from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://www.python.org/")
event_dict = {}
times = driver.find_elements(By.CSS_SELECTOR, value="#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul time")
names = driver.find_elements(By.CSS_SELECTOR, value="#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul a")
n = 0
for n in range(len(times)):
    date = times[n].get_attribute("datetime").split("T")[0]
    name = names[n].text
    event_dict[n] = {
        "time": date,
        "name": name,
    }
print(event_dict)
driver.quit()
