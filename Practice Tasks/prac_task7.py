from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://alnafi.com")
time.sleep(5)
driver.execute_script("window.open('https://google.com','new window')")
wins = driver.window_handles
time.sleep(2)
driver.switch_to.window(wins[0])
print("\n=================This is my zero index (alnafi)==============\n"+ driver.title)
mylanfi = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
print(mylanfi.text)
driver.switch_to.window(wins[1])
time.sleep(2)
print("\n=====================This is my first index(google)=====================\n " + driver.title)
mygoogle = driver.find_element(By.NAME, 'q')
print(mygoogle.text)
time.sleep(5)
driver.quit()