from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.selenium.dev/")
driver.switch_to.new_window("tab")
driver.get("https://playwright.dev/")
number_of_tabs = len(driver.window_handles)
print(f"Number of tabs opened: {number_of_tabs}")
current_tab = driver.current_window_handle
print(f"Current tab URL: {current_tab}")
driver.find_element(By.CSS_SELECTOR,".getStarted_Sjon").click()
first_tab = driver.window_handles[0]
if current_tab != first_tab:
    driver.switch_to.window(first_tab)

driver.find_element(By.XPATH, "//*[@id='main_navbar']/ul/li[2]/a/span").click()
time.sleep(3)