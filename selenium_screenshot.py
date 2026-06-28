from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import datetime
timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

driver_path = ChromeDriverManager().install()
service = Service(driver_path)

driver = webdriver.Chrome(service=service)
website_url = "https://google.com"
driver.get(website_url)
sleep(5)
driver.get_screenshot_as_file(f"Screenshot/{timestamp}_{website_url.replace('https://', '').replace('/', '_')}.png")  
sleep(2)
driver.quit()