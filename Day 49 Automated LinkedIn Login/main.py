from selenium import webdriver
from selenium.webdriver.common.by import By
import secrets
from selenium.webdriver.common.keys import Keys
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
# driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3839049333&geoId=104187078&keywords=python%20developer&location=Taiwan&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")
driver.get("https://www.linkedin.com/home")
time.sleep(10)
username = driver.find_element(By.ID, "session_key")
username.send_keys(secrets.USER)

password = driver.find_element(By.ID, "session_password")
password.send_keys(secrets.PASSWORD)

driver.find_element(By.XPATH, "//*[@id='main-content']/section[1]/div/div/form/div[2]/button").click()

while True:
    time.sleep(5)