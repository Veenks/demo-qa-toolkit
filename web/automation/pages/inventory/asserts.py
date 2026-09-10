"""InventoryPage — assertions (the 'Asserts' partial)."""
from playwright.sync_api import expect
from pages.inventory.map import InventoryPageMap


class InventoryPageAsserts(InventoryPageMap):
    def is_loaded(self):
        expect(self.page).to_have_url(self.URL)

    def expect_cart_badge_count(self, count: str):
        expect(self.cart_badge).to_have_text(count)

    def get_prices(self) -> list[float]:
        texts = self.product_prices.all_inner_texts()
        return [float(t.replace("$", "")) for t in texts]

    def expect_cart_badge_hidden(self):
        expect(self.cart_badge).to_have_count(0)
