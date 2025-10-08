from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.maximize_window()
# driver.minimize_window()
driver.fullscreen_window()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "p.oxd-text.oxd-text--p.orangehrm-login-forgot-header")
time.sleep(5)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
driver.close()


