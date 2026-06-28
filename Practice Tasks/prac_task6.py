from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.get("https://alnafi.com")
driver.maximize_window()
time.sleep(5)
driver.execute_script("window.open('https://google.com','new window')")
wins = driver.window_handles
time.sleep(2)
driver.switch_to.window(wins[0])
print("This is my zero index "+ driver.title)
driver.switch_to.window(wins[1])
time.sleep(2)
print("This is my first index " + driver.title)
time.sleep(5)
driver.quit()