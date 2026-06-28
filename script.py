from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
path=Service(r"chromedriver")
driver=webdriver.Chrome(service=path)
driver.get("https://www.apple.com/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Mac").click()
sleep(10)
driver.quit()