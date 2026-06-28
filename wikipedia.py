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
driver.get("https://www.wikipedia.org/" )
driver.maximize_window()
# <select id="searchLanguage" name="language">
# ... options omitted for brevity ...
# </select>
select = Select(driver.find_element(By.ID, "searchLanguage"))
select.select_by_visible_text("Türkçe")
count_of_languages = len(select.options)
print(f"Count of languages: {count_of_languages}")