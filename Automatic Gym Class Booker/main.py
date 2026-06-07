import os
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)

SITE_URL = "https://appbrewery.github.io/gym/"
ACCOUNT_EMAIL = ""
ACCOUNT_PASSWORD = ""

driver.get(SITE_URL)

wait = WebDriverWait(driver, timeout=2)


def retry(func, retries=20, description=None):
    for n in range(retries):
        print(f"Trying {description}. Attempt: {n + 1}")
        try:
            return func()
        except TimeoutException:
            if n == retries - 1:
                raise
            time.sleep(1)

def login():
    auth_btn = wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id='home-page']/section[1]/div/div/a[1]")))
    auth_btn.click()

    email_input = wait.until(ec.presence_of_element_located((By.NAME, "email")))
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys(ACCOUNT_PASSWORD)

    login_btn = driver.find_element(By.ID, "submit-button")
    login_btn.click()

retry(login, description="login")

class_booked = 0
waitlists_joined = 0
already_added_classes = 0
class_action_list = []

def book_class():
    global class_booked
    global waitlists_joined
    global already_added_classes
    global class_action_list

    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

    class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
    class_card_timings = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-'] p[id^='class-time-']")

    for i in range(len(class_cards)):
        class_day = class_cards[i].find_element(By.XPATH, "./ancestor::div[starts-with(@id, 'day-group-')]//h2[starts-with(@id, 'day-title-')]").text

        if class_card_timings[i].text.__contains__("6") and (class_day.__contains__("Tue") or class_day.__contains__("Thu")):
            class_title = class_cards[i].find_element(By.CSS_SELECTOR, "h3").text
            book_btn = class_cards[i].find_element(By.CSS_SELECTOR, "button")

            if book_btn.text == "Book Class":
                book_btn.click()
                class_booked += 1
                class_action_list.append(f"[New Booking] {class_title} on {class_day}")
                print(f"Successfully Booked: {class_title} on {class_day}")
            elif book_btn.text == "Join Waitlist":
                book_btn.click()
                waitlists_joined += 1
                class_action_list.append(f"[New Waitlist] {class_title} on {class_day}")
                print(f"Joined Waitlist for: {class_title} on {class_day}")
            elif book_btn.text == "Booked":
                book_btn.click()
                already_added_classes += 1
                print(f"Already Booked: {class_title} on {class_day}")
            elif book_btn.text == "Waitlisted":
                book_btn.click()
                already_added_classes += 1
                print(f"Already on Waitlist for: {class_title} on {class_day}")
            else:
                print("Error Button Text!")

retry(book_class, description="book class")

print("\n")
print("--- BOOKING SUMMARY ---")
print(f"Classes booked: {class_booked}")
print(f"Waitlists joined: {waitlists_joined}")
print(f"Already booked/waitlisted: {already_added_classes}")
print(f"Total Tuesday and Thursday 6pm classes processed: {class_booked + waitlists_joined + already_added_classes}")

print("\n")
print("--- DETAILED CLASS LIST ---")
for i in class_action_list:
    print(i)