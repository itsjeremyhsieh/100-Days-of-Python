from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("http://orteil.dashnet.org/experiments/cookie/")
timeout = time.time() + 5
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]
final_timeout = time.time() + 50*5
while time.time() <= final_timeout:
    if time.time() > timeout:
        timeout = time.time() + 5
        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
        store = driver.find_elements(By.CSS_SELECTOR, "#store b")
        prices = []
        for item in store:
            if item.text != "":
                cost = int(item.text.split("-")[1].strip().replace(",", ""))
                prices.append(cost)
        upgrades = {}
        for n in range(len(prices)):
            upgrades[prices[n]] = item_ids[n]

        affordable = {}
        for cost, id in upgrades.items():
            if money > cost:
                affordable[cost] = id
        highest = max(affordable)
        buy = affordable[highest]
        driver.find_element(By.ID, buy).click()

    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()
cps = driver.find_element(By.ID, "cps").text.split(":")[1]
print(f"Cookies/second: {cps}")
