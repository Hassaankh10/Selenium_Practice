from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://alnafi.com")
driver.maximize_window()
time.sleep(5)
print(driver.title)
driver.execute_script("window.open('https://google.com', 'new_window')")
driver.switch_to.window(driver.window_handles[1])
print(driver.title)
time.sleep(5)
driver.quit()