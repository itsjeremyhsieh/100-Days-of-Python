from selenium import webdriver
from selenium.webdriver.common.by import By
import userpass
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
# driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3839049333&geoId=104187078&keywords=python%20developer&location=Taiwan&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")
driver.get("https://tinder.com/")
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='q1887506695']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='q159125619']/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button").click()
time.sleep(3)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

driver.find_element(By.XPATH, "//*[@id='email']").send_keys(userpass.EMAIL)
password = driver.find_element(By.XPATH, "//*[@id='pass']")
password.send_keys(userpass.PASSWORD)
password.send_keys(Keys.ENTER)
time.sleep(5)
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(3)

driver.find_element(By.XPATH, "//*[@id='q159125619']/main/div[1]/div/div/div[3]/button[1]").click()
driver.find_element(By.XPATH, "//*[@id='q159125619']/main/div[1]/div/div/div[3]/button[2]").click()
try:
    driver.find_element(By.XPATH, "//*[@id='q1887506695']/div/div[2]/div/div/div[1]/div[1]/button").click()
except:
    pass
time.sleep(5)


while True:
    try:
        driver.find_element(By.XPATH, '//body').send_keys(Keys.ARROW_RIGHT)
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)
    except NoSuchElementException:
        time.sleep(2)
