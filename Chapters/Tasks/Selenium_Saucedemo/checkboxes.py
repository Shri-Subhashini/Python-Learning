from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

checked_count = 1
browser = webdriver.Chrome()
browser.get("https://www.hackerrank.com/auth/login")
browser.maximize_window()
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
checkboxes = browser.find_element(By.XPATH, "//*[@id='remember-me']").click()
time.sleep(3)
browser.find_element(By.XPATH, "//*[@id='remember-me']").click()
# checkboxes = browser.find_elements(By.XPATH, "//"input[@type = 'checkbox']")
# for checkbox in checkboxes:
#     checkbox.send_keys(Keys.SPACE)

# 
# for checkbox in checkboxes:
#     if checkbox.is_selected():
#         checked_count += 1

expected_check_count = 1
assert checked_count == expected_check_count, f"Expected {expected_check_count} checkbox to be checked, but found {checked_count}."        
time.sleep(3)
0