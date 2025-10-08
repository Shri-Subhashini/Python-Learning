from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.maximize_window()
driver.execute_script("window.scrollTo(0, 500);")
table = driver.find_element(By.ID, "countries")
rows = table.find_elements(By.TAG_NAME, "tr")
row_count = len(rows)
print("Total number of rows in the table:", row_count)
target_value = "India"
found = False
for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        if cell.text == target_value:
            print(f"Found '{target_value}' in the table.")
            found = True
            break
    if found:
        break
if not found:
    print(f"'{target_value}' not found in the table.")
time.sleep(3)