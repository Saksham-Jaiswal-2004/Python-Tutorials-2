from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")

# articles = driver.find_element(By.XPATH, "//*[@id='articlecount']/ul/li[2]/a[1]")
# print(articles.text)
# articles.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

# search_btn = driver.find_element(By.CLASS_NAME, "search-toggle")
# search_btn.send_keys(Keys.ENTER)
#
# search_bar = driver.find_element(By.NAME, "search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
submit = driver.find_element(By.CLASS_NAME, "btn")

first_name.send_keys("Saksham")
last_name.send_keys("Jaiswal")
email.send_keys("sakshamjaiswalofficial@gmail.com")
submit.send_keys(Keys.ENTER)

# driver.quit()