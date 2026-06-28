from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
path = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=path)
driver.get("https://www.apple.com/")
driver.maximize_window()
driver.quit()   