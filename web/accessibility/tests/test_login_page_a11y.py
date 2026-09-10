"""Accessibility scan of the Sauce Demo login page."""
from lib.axe_helper import run_axe, assert_no_violations

URL = "https://www.saucedemo.com/"


def test_login_page_has_no_critical_or_serious_violations(page):
    page.goto(URL)
    results = run_axe(page)
    assert_no_violations(results)
