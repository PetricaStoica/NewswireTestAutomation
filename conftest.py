import pytest
from utils.browser import Browser
from pages.login_page import LoginPage
from playwright.sync_api import expect

@pytest.fixture(scope='session')
def browser():
    browser = Browser()
    yield browser.page
    browser.close()

@pytest.fixture(scope='function')
def login(browser):
    login_page = LoginPage(browser)
    home_url = 'https://newswire.storyful.com'
    
    def is_logged_in():
        current_url = browser.url
        if home_url in current_url:
            return True
        return False
    
    if not is_logged_in():
        login_page.goto(home_url)
        login_page.login('john.doe@automation.com', 'Password123!')
        # Wait for navigation to complete
        browser.wait_for_load_state('networkidle')
    
    yield browser
