import pytest 
from playwright.sync_api import sync_playwright

def pytest_addoption(parser):
    parser.addoption("--username", action = "append", default = [], help = " List of username")
    parser.addoption("--password", action = "append", default = [], help = "List of password")

def pytest_generate_tests(metafunc):
    usernames = metafunc.config.getoption("username")
    passwords = metafunc.config.getoption("password")

    if "username" in metafunc.fixturenames and "password" in metafunc.fixturenames:
        if len(usernames) != len(passwords):
            raise ValueError("Usernames and passwords must match.")
        metafunc.parametrize("username,password", zip(usernames, passwords))


@pytest.fixture(scope="function")
def browser_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

        
