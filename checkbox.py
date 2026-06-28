from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("file:///path/to/checkbox_test_site.html")
driver.maximize_window()
basic_section = driver.find_element(By.ID, "basic-section")
# //*[@id="cb1"]
checkboxes = basic_section.find_elements(By.XPATH, ".//input[@type='checkbox']")
count = 0
for checkbox in checkboxes:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(checkbox))
    if not checkbox.is_selected():
        checkbox.click()
        sleep(0.3)
    count += 1
sleep(3)
print(f"Count of checkboxes: {count}")

select_all_button = driver.find_element(By.ID, "select-all")
driver.execute_script("arguments[0].click();", select_all_button)
sleep(1)

driver.find_element(By.ID, "agree1").click()
sleep(1)
driver.find_element(By.ID, "submit-btn").click()
sleep(1)


driver.quit()