from selenium import webdriver
from selenium.webdriver.common.by import By
import time


username = "admin"
password = "admin"

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://admin:admin@the-internet.herokuapp.com/basic_auth"
driver.get(url)
time.sleep(5)
driver.quit()


