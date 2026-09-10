"""CartPage — user actions (the 'Actions' partial)."""
from pages.cart.map import CartPageMap


class CartPageActions(CartPageMap):
    def checkout(self):
        self.checkout_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()
