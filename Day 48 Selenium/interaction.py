from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# count.click()
time.sleep(5)
search = driver.find_element(By.ID, "searchInput")

search.send_keys("Python")
search.send_keys(Keys.ENTER)
time.sleep(3)
