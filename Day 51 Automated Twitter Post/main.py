from selenium import webdriver
from selenium.webdriver.common.by import By
import userpass
import time

PROMISED_DOWN = 150
PROMISED_UP = 10

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://speed.one/")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='start-button']/div/button").click()
        time.sleep(50)
        download = self.driver.find_element(By.XPATH, "//*[@id='result_download_val']").text
        upload = self.driver.find_element(By.XPATH, "//*[@id='result_upload_val']").text
        return download, upload
    def tweet_at_provider(self, download, upload):
        msg = f"Hey Internet Provider, why is my internet speed {download}down/{upload}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        self.driver.get("https://twitter.com/home")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input").send_keys(userpass.TWITTER_EMAIL)
        self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div").send_keys(userpass.TWITTER_PASSWORD)
        self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div").send_keys(msg)
        self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]").click()
        time.sleep(5)


IST = InternetSpeedTwitterBot()
download, upload = IST.get_internet_speed()
IST.tweet_at_provider(download, upload)
while True:
    time.sleep(10)