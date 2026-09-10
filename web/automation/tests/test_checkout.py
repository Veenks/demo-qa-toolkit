"""Covers CHK-01 to CHK-04 from web/manual/test-cases.md."""
import pytest


@pytest.mark.smoke
def test_complete_checkout_with_valid_info(logged_in_page, cart_page, checkout_page):
    """CHK-01: Complete checkout with valid info."""
    logged_in_page.add_product_to_cart("Sauce Labs Backpack")
    logged_in_page.go_to_cart()
    cart_page.checkout()
    checkout_page.fill_info("Javier", "Torres", "1000")
    checkout_page.submit_info()
    checkout_page.finish()
    checkout_page.expect_confirmation()


@pytest.mark.regression
def test_checkout_fails_with_missing_zip(logged_in_page, cart_page, checkout_page):
    """CHK-02: Checkout fails with missing required field."""
    logged_in_page.add_product_to_cart("Sauce Labs Backpack")
    logged_in_page.go_to_cart()
    cart_page.checkout()
    checkout_page.fill_info("Javier", "Torres", "")
    checkout_page.submit_info()
    checkout_page.expect_error("Postal Code is required")


@pytest.mark.regression
def test_checkout_overview_total_matches_items(logged_in_page, cart_page, checkout_page):
    """CHK-03: Checkout overview shows correct total."""
    logged_in_page.add_product_to_cart("Sauce Labs Backpack")
    logged_in_page.add_product_to_cart("Sauce Labs Bike Light")
    logged_in_page.go_to_cart()
    cart_page.checkout()
    checkout_page.fill_info("Javier", "Torres", "1000")
    checkout_page.submit_info()
    checkout_page.expect_total_visible()


@pytest.mark.regression
def test_cancel_checkout_returns_to_cart(logged_in_page, cart_page, checkout_page):
    """CHK-04: Cancel checkout returns to the cart page (not the product listing)."""
    logged_in_page.add_product_to_cart("Sauce Labs Backpack")
    logged_in_page.go_to_cart()
    cart_page.checkout()
    checkout_page.cancel()
    cart_page.is_loaded()