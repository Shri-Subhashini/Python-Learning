from selenium import webdriver
import time


viewports = [(1024, 768), (786, 1024), (375, 667), (414, 896)]

driver = webdriver.Chrome()
driver.get("https://www.google.com ")

try:
    for width, height in viewports:
        driver.set_window_size(width, height)
        time.sleep(3)
finally:
    driver.close()


