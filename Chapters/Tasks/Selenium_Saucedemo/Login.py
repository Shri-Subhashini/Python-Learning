import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()
username = "standard_user"
password = "secret_sauce"
login_url = "https://www.saucedemo.com/"
driver.get(login_url)   

username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")

username_field.send_keys(username)
password_field.send_keys(password)

login_button = driver.find_element(By.ID, "login-button")
assert not login_button.get_attribute("disabled")
login_button.click()
success_element = driver.find_element(By.CSS_SELECTOR, ".title")
print("Success element: ", success_element.text)
# success_element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, ".title"))
# )
assert success_element.text == "Products", "Login failed or incorrect page title"

time.sleep(3)
driver.quit()



