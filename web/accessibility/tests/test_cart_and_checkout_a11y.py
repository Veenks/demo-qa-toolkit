"""Accessibility scan of the cart and checkout flow."""
from lib.axe_helper import run_axe, assert_no_violations

LOGIN_URL = "https://www.saucedemo.com/"


def _login(page):
    page.goto(LOGIN_URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_url("**/inventory.html")


def test_cart_page_has_no_critical_or_serious_violations(page):
    _login(page)
    page.click(".shopping_cart_link")
    page.wait_for_url("**/cart.html")

    results = run_axe(page)
    assert_no_violations(results)


def test_checkout_info_page_has_no_critical_or_serious_violations(page):
    _login(page)
    page.locator(".inventory_item", has_text="Sauce Labs Backpack").get_by_role(
        "button", name="Add to cart"
    ).click()
    page.click(".shopping_cart_link")
    page.click("#checkout")
    page.wait_for_url("**/checkout-step-one.html")

    results = run_axe(page)
    assert_no_violations(results)
