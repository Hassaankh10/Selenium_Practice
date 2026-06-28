from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

# Use incognito mode to start fresh
options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("http://YOUR_JELLYFIN_SERVER_URL" )
driver.maximize_window()
# Wait for elements to be present
wait = WebDriverWait(driver, 20)
sleep(10)
username = wait.until(EC.presence_of_element_located((By.ID, "txtManualName")))
password = wait.until(EC.presence_of_element_located((By.ID, "txtManualPassword")))
username.send_keys("YOUR_USERNAME")
# sleep(2)
driver.implicitly_wait(2)

password.send_keys("YOUR_PASSWORD")
# sleep(2)
driver.implicitly_wait(2)
# <button is="emby-button" type="submit" class="raised button-submit block emby-button"> <span>Sign In</span> </button>
# //*[@id="loginPage"]/div/form/button
login_button = driver.find_element(By.XPATH, '//*[@id="loginPage"]/div/form/button')
login_button.click()
driver.implicitly_wait(5)
driver.quit()