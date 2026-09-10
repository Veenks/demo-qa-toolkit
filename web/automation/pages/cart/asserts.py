"""CartPage — assertions (the 'Asserts' partial)."""
from playwright.sync_api import expect
from pages.cart.map import CartPageMap


class CartPageAsserts(CartPageMap):
    def is_loaded(self):
        expect(self.page).to_have_url(self.URL)

    def expect_item_count(self, count: int):
        expect(self.cart_items).to_have_count(count)
