"""Combines Map, Actions, and Asserts into a single InventoryPage class."""
from pages.inventory.actions import InventoryPageActions
from pages.inventory.asserts import InventoryPageAsserts


class InventoryPage(InventoryPageActions, InventoryPageAsserts):
    pass
