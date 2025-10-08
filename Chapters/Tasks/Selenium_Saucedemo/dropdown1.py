from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome()
driver.maximize_window()
login_url = "https://the-internet.herokuapp.com/dropdown"
driver.get(login_url)
dropdown_element = driver.find_element(By.ID, "dropdown")

#1st method

# select = Select(dropdown_element)
# option_count = len(select.options)
# # Select value by visible txt
# # select.select_by_visible_text("Option 2")

# #Select value by index
# # select.select_by_index(1)

# #Select option by value
# select.select_by_value("2")

# expected_count = 3
# assert option_count == expected_count, f"Expected {expected_count} options, but found {option_count}."
# time.sleep(3)

#2nd method
target_value = "Option 2"
select = Select(dropdown_element)
for option in select.options:
    if option.text == target_value:
        option.click()
        break
    else:
        print(f"Option with text '{target_value}' not found in the dropdown.")

time.sleep(3)   




