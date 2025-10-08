from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()
url = "https://www.globalsqa.com/demo-site/datepicker/"
driver.maximize_window()
driver.get(url)

driver.find_element(By.XPATH, "//*[@id='post-2661']/div[2]/div/div/div[1]/div").click()
frameLo = driver.find_element(By.XPATH, "//*[@id='post-2661']/div[2]/div/div/div[1]/p/iframe")
driver.switch_to.frame(frameLo)
time.sleep(3)
driver.find_element(By.ID, "datepicker").click()

current_date = datetime.now()
next_date = current_date + timedelta(days=1)
formatted_date = next_date.strftime("%m/%d/%Y")
driver.find_element(By.ID, "datepicker").send_keys(formatted_date + Keys.TAB)
time.sleep(3)
driver.quit()

