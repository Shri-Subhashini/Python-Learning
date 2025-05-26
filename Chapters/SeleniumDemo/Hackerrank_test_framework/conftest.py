import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def pytest_addoption(parser):
    parser.addoption("--username", action="append", default=[], help="List of usernames")
    parser.addoption("--password", action="append", default=[], help="List of passwords")

def pytest_generate_tests(metafunc):
    usernames = metafunc.config.getoption("username")
    passwords = metafunc.config.getoption("password")

    if "username" in metafunc.fixturenames and "password" in metafunc.fixturenames:
        if len(usernames) != len(passwords):
            raise ValueError("Usernames and passwords must match.")
        metafunc.parametrize("username,password", zip(usernames, passwords))

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()
