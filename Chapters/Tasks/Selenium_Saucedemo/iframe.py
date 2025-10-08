from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")

iframe = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(iframe)


text_editor = driver.find_element(By.ID, "tinymce")

text_editor.send_keys("Hello Virat")
time.sleep(8)

# To interact again with elements outside the iframe (in the main HTML document), you must explicitly switch back using:
# driver.switch_to.default_content()
