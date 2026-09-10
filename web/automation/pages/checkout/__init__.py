"""Combines Map, Actions, and Asserts into a single CheckoutPage class."""
from pages.checkout.actions import CheckoutPageActions
from pages.checkout.asserts import CheckoutPageAsserts


class CheckoutPage(CheckoutPageActions, CheckoutPageAsserts):
    pass
