from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.amazon.in/ORILEY-Vermicompost-Organic-Fertilizer-Natural/dp/B0CMZSRRW8/ref=pd_rhf_gw_s_pd_crcd_d_sccl_1_4/525-4256327-0198141?pd_rd_w=JqwDR&content-id=amzn1.sym.7edc8fe7-49c8-4837-acf4-779a8e8647e2&pf_rd_p=7edc8fe7-49c8-4837-acf4-779a8e8647e2&pf_rd_r=62NCYB7DZGSBFVEH964T&pd_rd_wg=0ISYj&pd_rd_r=c7ef13f1-5385-4e76-b877-f5984a238148&pd_rd_i=B0CMZSRRW8&th=1")
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole").text
# print(price_dollar)

search_bar = driver.find_element(By.NAME, "q")
print(search_bar)
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, "submit")
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, "//*[@id='site-map']/div[2]/div/ul/li[3]/a")
print(bug_link.text)

# Only closes a particular tab
# driver.close()

# Closes complete browser
driver.quit()