from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time 

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://demo.automationtesting.in/Register.html"
driver.get(url)

# For  ouse movements
actions = ActionChains(driver)

hover_element =  driver.find_element(By.XPATH, "//*[@id='header']/nav/div/div[2]/ul/li[4]/a")
time.sleep(3)
actions.move_to_element(hover_element).perform()
driver.find_element(By.XPATH, "//*[@id='header']/nav/div/div[2]/ul/li[4]/ul/li[3]/a").click()

time.sleep(3)
driver.quit()