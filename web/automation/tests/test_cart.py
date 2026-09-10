"""Covers CART-01 to CART-04 from web/manual/test-cases.md."""
import pytest


@pytest.mark.smoke
def test_add_single_item_to_cart(logged_in_page):
    """CART-01: Add single item to cart."""
    logged_in_page.add_product_to_cart("Sauce Labs Backpack")
    logged_in_page.expect_cart_badge_count("1")


@pytest.mark.regression
def test_remove_item_from_cart(logged_in_page):
    """CART-02: Remove item from cart."""
    logged_in_page.add_product_to_cart("Sauce Labs Backpack")
    logged_in_page.remove_product_from_cart("Sauce Labs Backpack")
    logged_in_page.expect_cart_badge_hidden()


@pytest.mark.regression
def test_cart_badge_reflects_multiple_items(logged_in_page):
    """CART-03: Cart badge reflects multiple items."""
    for product in ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt"]:
        logged_in_page.add_product_to_cart(product)
    logged_in_page.expect_cart_badge_count("3")


@pytest.mark.regression
def test_cart_persists_after_continue_shopping(logged_in_page, cart_page):
    """CART-04: Cart persists after navigating back."""
    logged_in_page.add_product_to_cart("Sauce Labs Backpack")
    logged_in_page.go_to_cart()
    cart_page.is_loaded()
    cart_page.continue_shopping()
    logged_in_page.is_loaded()
    logged_in_page.expect_cart_badge_count("1")
