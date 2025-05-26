import allure
import functools

# def login_test_metadata():
#     """Reusable Allure metadata for login tests"""
#     def decorator(func):
#         func = allure.feature("Login Feature")(func)
#         func = allure.story("Valid and Invalid Logins")(func)
#         func = allure.severity(allure.severity_level.CRITICAL)(func)
#         return func
#     return decorator



# def login_test_metadata():
#     """Reusable Allure metadata for login tests"""
#     def decorator(func):
#         @allure.feature("Login Feature")
#         @allure.story("Valid and Invalid Logins")
#         @allure.severity(allure.severity_level.CRITICAL)
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator

# def login_test_metadata():
#     """Reusable Allure metadata for login tests using dynamic API"""
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             allure.dynamic.feature("Login Feature")
#             allure.dynamic.story("Valid and Invalid Logins")
#             allure.dynamic.severity(allure.severity_level.CRITICAL)
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator


import allure

def pytest_runtest_setup(item):
    if 'login_test' in item.keywords:
        allure.dynamic.feature("Login Feature")
        allure.dynamic.story("Valid and Invalid Logins")
        allure.dynamic.severity(allure.severity_level.CRITICAL)

