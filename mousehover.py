from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.flipkart.com/laptops/~cs-q9dxe5icqw/pr?sid=6bo%2Cb5g&collection-tab-name=HP%20Victus%20RTX%203050&sort=price_asc&param=8267&BU=CoreElectronics")
driver.maximize_window()
time.sleep(3)

tvappliance = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/span[2]")
action = ActionChains(driver)
action.move_to_element(tvappliance).perform()
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Air Conditioners").click()
time.sleep(8)
driver.quit()