"""LoginPage — element locators (the 'Map' partial).

Only locators live here. No actions, no assertions — just knowing where
things are on the page.
"""
from playwright.sync_api import Page


class LoginPageMap:
    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")
