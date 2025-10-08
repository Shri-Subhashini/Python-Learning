from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url)

# Switch to simple JS Alerts
alert_button = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[1]/button")
alert_button.click()
alert = driver.switch_to.alert
alert_text = alert.text
print("Alert text:", alert_text)

# To accept the alerts
time.sleep(3)
alert.accept()
time.sleep(3)


# Switch to confirmation JS Alerts

alert_button = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[2]/button")
alert_button.click()
alert = driver.switch_to.alert
alert_text = alert.text
print("Alert confirm text:", alert_text)

# To accept the alerts
time.sleep(3)
alert.accept()
time.sleep(3)


# Switch to prompt JS Alerts

alert_button = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button")
alert_button.click()
alert = driver.switch_to.alert
alert_text = alert.text
print("Alert promt text:", alert_text)
time.sleep(5)
alert.send_keys("Hello Virat")

# To accept the alerts
time.sleep(3)
alert.accept()
time.sleep(3)
