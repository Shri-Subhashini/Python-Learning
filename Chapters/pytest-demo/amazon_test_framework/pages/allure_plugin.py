import allure

def pytest_runtest_setup(item):
    if 'login_test' in item.keywords:
        allure.dynamic.feature("Login Feature")
        allure.dynamic.story("Valid and Invalid Logins")
        allure.dynamic.severity(allure.severity_level.CRITICAL)

