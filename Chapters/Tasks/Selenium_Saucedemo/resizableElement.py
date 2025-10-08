from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Resizable.html")
resizable_element = driver.find_element(By.XPATH, "//*[@id='resizable']/div[3]")
initial_element_size = driver.find_element(By.XPATH, "//*[@id='resizable']")
initial_size = initial_element_size.size
print(f"Initial size: {initial_size}")

time.sleep(3)

actions = ActionChains(driver)
actions.click_and_hold(resizable_element).move_by_offset(100, 100).release().perform()
time.sleep(5)
resized_element = initial_element_size.size
print(f"Resized size: {resized_element}")

driver.quit()