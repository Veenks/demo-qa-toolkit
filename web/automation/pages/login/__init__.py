"""Combines the Map, Actions, and Asserts partials into a single LoginPage class.

This file is the only place that assembles the pieces — everything else
in this folder only knows about its own concern.
"""
from pages.login.actions import LoginPageActions
from pages.login.asserts import LoginPageAsserts


class LoginPage(LoginPageActions, LoginPageAsserts):
    pass
