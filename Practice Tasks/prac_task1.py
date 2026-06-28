from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://m.cricbuzz.com/cricket-stats/icc-rankings/men/batting")
driver.maximize_window()
time.sleep(3)

ranktable=driver.find_element(By.XPATH, "/html/body/div/main/div[2]/div[1]/div/div/div[2]")

batsmen = ranktable.find_elements(By.XPATH, ".//a[contains(@href, '/profiles/')]")
print(f"Number of batsmen on the page: {len(batsmen)}")
