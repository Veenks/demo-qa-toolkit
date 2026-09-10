"""InventoryPage — element locators (the 'Map' partial)."""
from playwright.sync_api import Page


class InventoryPageMap:
    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, page: Page):
        self.page = page
        self.product_items = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator(".product_sort_container")
        self.product_prices = page.locator(".inventory_item_price")
