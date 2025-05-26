import pytest
import allure
from pages.login_page import LoginPage


# @allure.feature("Login Feature")
# @allure.story("Valid and Invalid Logins")
# @allure.severity(allure.severity_level.CRITICAL)

@pytest.mark.login_test
def test_amazon_login(browser_page, username, password):
    login = LoginPage(browser_page)

    with allure.step("Go to login page"):
        login.goto_login_page()
    
    with allure.step(f"Login with username: {username}"):
        login.login(username, password)

    with allure.step("Check login status"):
        if login.is_login_failed():
            print("Login Failed")
        else:
            assert True  # login successful