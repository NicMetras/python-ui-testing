import pytest
from pages.login_page import LoginPage
 
def test_login_successful(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in browser.current_url

def test_login_negative(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("negative_case", "bad_sauce")
    assert "Epic sadface: Username and password do not match any user in this service" in login_page.get_error_message()    


