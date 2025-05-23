from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://www.saucedemo.com/"
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, 'h3[data-test="error"]')

    def load(self):
        self.browser.get(self.url)

    def enter_username(self, username):
        self.browser.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.browser.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.browser.find_element(*self.login_button).click()
    
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.browser.find_element(*self.error_message).text