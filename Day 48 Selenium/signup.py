from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Jeremy")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Hsieh")

email = driver.find_element(By.NAME, "email")
email.send_keys("jeremy.life0107@gmail.com")

submit = driver.find_element(By.CLASS_NAME, "btn")
submit.click()

time.sleep(5)