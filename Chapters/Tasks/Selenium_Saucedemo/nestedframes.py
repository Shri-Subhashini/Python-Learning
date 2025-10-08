from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/nested_frames")

# Switch to the top frame
driver.switch_to.frame("frame-top")

# Switch to the middle 
driver.switch_to.frame("frame-middle")
content_middle = driver.find_element(By.ID, "content")
print("Content of the middle frame:", content_middle.text)

# Switch to Default content
driver.switch_to.default_content()

# Switch to the bottom frame
driver.switch_to.frame("frame-bottom")
content_bottom = driver.find_element(By.TAG_NAME, "body").text
print("Content of the bottom frame:", content_bottom)

time.sleep(3)

# First go into the parent frame and frm there move to the middle frame; then come out from the current frame and again move to bottom frame.
# driver.switch_to.default_content() -> here, coming out of all nested frames, including both frame-middle and its parent frame-top.

#  If you wanted to go up just one level (i.e., from frame-middle to frame-top), you'd use:
# driver.switch_to.parent_frame()
