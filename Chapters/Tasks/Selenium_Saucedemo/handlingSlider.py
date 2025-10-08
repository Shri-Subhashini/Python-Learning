from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/horizontal_slider")
slider = driver.find_element(By.XPATH, "//input[@type='range']")
actions = ActionChains(driver)

# Move the slider to the right by 0.5 units
actions.click_and_hold(slider).move_by_offset(100,0).release().perform()
time.sleep(5)
driver.quit()
