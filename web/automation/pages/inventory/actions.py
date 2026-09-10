"""InventoryPage — user actions (the 'Actions' partial)."""
from pages.inventory.map import InventoryPageMap


class InventoryPageActions(InventoryPageMap):
    def add_product_to_cart(self, product_name: str):
        item = self.page.locator(".inventory_item", has_text=product_name)
        item.get_by_role("button", name="Add to cart").click()

    def remove_product_from_cart(self, product_name: str):
        item = self.page.locator(".inventory_item", has_text=product_name)
        item.get_by_role("button", name="Remove").click()

    def sort_by(self, option_label: str):
        self.sort_dropdown.select_option(label=option_label)

    def go_to_cart(self):
        self.cart_link.click()
