import time
from playwright.sync_api import expect
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email_input = "input[name='username']"  
        self.password_input = "input[name='password']"  
        self.login_button = "[data-hr-focus-item='private']:text-is('Log In')"
        self.error_message = "Invalid login or password. Please try again."

    def goto_login_page(self):
        # self.page.goto("https://www.hackerrank.com/auth/login")
        self.page.goto("https://www.hackerrank.com/auth/login")
        self.page.wait_for_load_state() 

    def login(self, username, password): 
        self.page.fill(self.email_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
        time.sleep(5)
        
    
    def is_login_failed(self):
        self.page.locator("p:has-text('Invalid login or password. Please try again.')").is_visible()

    def is_login_success(self):
        return self.page.url.startswith("https://www.hackerrank.com/dashboard")

        # https://www.hackerrank.com/dashboard     https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index

        # To run with allure report : pytest testss\test_login.py --alluredir=allure-results --clean-alluredir --username subha.krs7@gmail.com --password Subhavirat
        # To run: pytest testss\test_login.py --username subha.krs7@gmail.com --password Subhavirat
