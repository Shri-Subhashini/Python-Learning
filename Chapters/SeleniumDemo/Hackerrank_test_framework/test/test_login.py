# import selenium
# from webdriver_manager.chrome import ChromeDriverManager


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager

# # Setup Chrome browser
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# # Open a website
# driver.get("https://www.google.com")

# # Print the page title
# print("Title is:", driver.title)

# # Close the browser
# driver.quit()



import pytest
import allure
from pages.login_page import LoginPage
# from pages.allure_plugin import login_test_metadata



# @allure.feature("Login Feature")
# @allure.story("Valid and Invalid Logins")
# @allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.login_test
def test_hackerrank_login(driver, username, password):
    login = LoginPage(driver)

    with allure.step("Go to login page"):
        login.goto_login_page()

    with allure.step(f"Login with username: {username}"):
        login.login(username, password)

    with allure.step("Check login status"):
        if login.is_login_failed():
            print("Login Failed")
            assert False
        else:
            assert login.is_login_success()
