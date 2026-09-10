"""Accessibility scan of the Sauce Demo product listing page, logged in."""
from lib.axe_helper import run_axe, assert_no_violations

LOGIN_URL = "https://www.saucedemo.com/"


def test_inventory_page_has_no_critical_or_serious_violations(page):
    page.goto(LOGIN_URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_url("**/inventory.html")

    results = run_axe(page)
    assert_no_violations(results)
