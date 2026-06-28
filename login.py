from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.saucedemo.com/" )
driver.maximize_window()
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")
username.send_keys("problem_user")
sleep(2)
password.send_keys("secret_sauce")
sleep(2)
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
sleep(5)
driver.quit()