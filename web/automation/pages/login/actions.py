"""LoginPage — user actions (the 'Actions' partial).

Verbs only: what a user can DO on this page. No assertions here.
"""
from pages.login.map import LoginPageMap


class LoginPageActions(LoginPageMap):
    def goto(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
