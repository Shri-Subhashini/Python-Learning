from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.NAME, 'username')
        self.password_input = (By.NAME, 'password')
        self.login_button = (By.XPATH, "//button[normalize-space()='Log In']")
        self.error_message_text = "Invalid login or password. Please try again."

    def goto_login_page(self):
        self.driver.get("https://www.hackerrank.com/auth/login")

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.email_input)).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def is_login_failed(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, f"//p[contains(text(), '{self.error_message_text}')]"))
            )
            return True
        except:
            return False

    def is_login_success(self):
        return self.driver.current_url.startswith("https://www.hackerrank.com/dashboard")
