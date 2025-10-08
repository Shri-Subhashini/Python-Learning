from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

csv_file = "testData.csv"

# Creating empty list
test_data = []
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        test_data.append(row)

print(test_data)

for data in test_data:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(3)
    driver.find_element(By.ID, "user-name").send_keys(data['username'])
    driver.find_element(By.ID, "password").send_keys(data['password'])
    driver.find_element(By.ID, "login-button").click()
    time.sleep(4)
