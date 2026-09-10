"""CartPage — element locators (the 'Map' partial)."""
from playwright.sync_api import Page


class CartPageMap:
    URL = "https://www.saucedemo.com/cart.html"

    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")
        self.continue_shopping_button = page.locator("#continue-shopping")
