from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import selections
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
# Use incognito mode to start fresh
options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://alnafi.com/")
driver.maximize_window()

# //*[@id="footer-section"]/div/div[2]
footer = driver.find_element(By.XPATH, '//*[@id="footer-section"]/div/div[2]')
for link in footer.find_elements(By.TAG_NAME, "a"):
    print(link.text)

