from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.maximize_window()
url = "https://demo.automationtesting.in/Datepicker.html"
driver.get(url)
driver.find_element(By.ID, "datepicker2").click()
current_date = datetime.now()
print("Current date: ", current_date)
next_date = current_date + timedelta(days=1)
next_day_str = (str(next_date.day))
print("Next day: ", next_day_str)
current_month = datetime.now().month
print("Current month: ", current_month)
current_year = datetime.now().year
print("Current Year: ",current_year)
next_month = (current_month % 12) + 1
print("Next month: ",next_month)
next_month_year = f"{next_month}/{current_year}"
print("Next month Year: ",next_month_year)
month_dropdown = driver.find_element(By.CSS_SELECTOR, ".datepick-month-year")
select = Select(month_dropdown)
select_month_year = select.select_by_value(str(next_month_year))
print("Select month Year :",select_month_year)
year_dropdown = driver.find_element(By.CSS_SELECTOR,".datepick-month-year")
select = Select(year_dropdown)
for option in select.options:
    print(option.text)

# select.select_by_visible_text("2025")
driver.find_element(By.LINK_TEXT, next_day_str).click()
time.sleep(3)