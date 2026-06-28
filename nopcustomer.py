from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
wait = WebDriverWait(driver, 20)

# Login
driver.get("https://admin-demo.nopcommerce.com/Admin/login")

driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Navigate to customer list
wait.until(EC.url_contains("/Admin"))
driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")

# Click Search and wait for results table to populate
wait.until(EC.element_to_be_clickable((By.ID, "search-customers"))).click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#customers-grid tbody tr")))

# Count and click all checkboxes
checkboxes = driver.find_elements(By.NAME, "checkbox_customers")
count = 0
for checkbox in checkboxes:
    wait.until(EC.element_to_be_clickable(checkbox))
    checkbox.click()
    sleep(0.3)
    count += 1

print(f"Count of checkboxes: {count}")

sleep(3)
driver.quit()
