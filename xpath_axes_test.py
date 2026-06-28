from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

# ── open the HTML file ──────────────────────────────────────────────
path = os.path.abspath("xpath_axes_demo.html")   # must be in same folder
service = Service(os.path.join(os.path.dirname(os.path.abspath(__file__)), "chromedriver"))
driver = webdriver.Chrome(service=service)
driver.get(f"file:///{path}")
print(f"\nOpened: {path}\n{'='*55}")

# ── helper ──────────────────────────────────────────────────────────
def show(label, elements):
    texts = [el.get_attribute("id") or el.text or el.tag_name for el in elements]
    print(f"{label:<25} → {texts}")

# ── 1. SELF ─────────────────────────────────────────────────────────
show("self", driver.find_elements(By.XPATH, "//div[@id='target-element']/self::div"))

# ── 2. PARENT ───────────────────────────────────────────────────────
show("parent", driver.find_elements(By.XPATH, "//div[@id='target-element']/parent::div"))

# ── 3. ANCESTOR ─────────────────────────────────────────────────────
show("ancestor", driver.find_elements(By.XPATH, "//div[@id='target-element']/ancestor::div"))

# ── 4. CHILD ────────────────────────────────────────────────────────
show("child", driver.find_elements(By.XPATH, "//div[@id='outer']/child::div"))

# ── 5. DESCENDANT ───────────────────────────────────────────────────
show("descendant", driver.find_elements(By.XPATH, "//div[@id='outer']/descendant::div"))

# ── 6. PRECEDING-SIBLING ────────────────────────────────────────────
# sibling-2 is the current → preceding-sibling = sibling-1 only
show("preceding-sibling", driver.find_elements(By.XPATH, "//div[@id='sibling-2']/preceding-sibling::div"))

# ── 7. FOLLOWING-SIBLING ────────────────────────────────────────────
# sibling-2 is current → following-sibling = sibling-3 only
show("following-sibling", driver.find_elements(By.XPATH, "//div[@id='sibling-2']/following-sibling::div"))

# ── 8. PRECEDING ────────────────────────────────────────────────────
# from password field → find email input (comes before it in the page)
show("preceding", driver.find_elements(By.XPATH, "//input[@id='password']/preceding::input[@id='email']"))

# ── 9. FOLLOWING ────────────────────────────────────────────────────
# from password field → find confirmPassword input (comes after it)
show("following", driver.find_elements(By.XPATH, "//input[@id='password']/following::input[@id='confirmPassword']"))

print(f"\n{'='*55}")
print("Done! All axes tested.")
driver.quit()
