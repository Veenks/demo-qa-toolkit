"""Combines Map, Actions, and Asserts into a single CartPage class."""
from pages.cart.actions import CartPageActions
from pages.cart.asserts import CartPageAsserts


class CartPage(CartPageActions, CartPageAsserts):
    pass
