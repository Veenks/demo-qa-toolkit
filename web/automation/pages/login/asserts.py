"""LoginPage — assertions (the 'Asserts' partial).

Verification only: what we can CHECK is true about this page's state.
"""
from playwright.sync_api import expect
from pages.login.map import LoginPageMap


class LoginPageAsserts(LoginPageMap):
    def expect_error(self, text: str):
        expect(self.error_message).to_contain_text(text)
