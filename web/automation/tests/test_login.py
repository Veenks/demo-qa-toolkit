"""Covers LOGIN-01 to LOGIN-04 from web/manual/test-cases.md."""
import pytest
from conftest import STANDARD_USER, PASSWORD


@pytest.mark.smoke
def test_successful_login_standard_user(login_page, inventory_page):
    """LOGIN-01: Successful login with standard user."""
    login_page.goto()
    login_page.login(STANDARD_USER, PASSWORD)
    inventory_page.is_loaded()


@pytest.mark.regression
def test_login_fails_with_invalid_password(login_page):
    """LOGIN-02: Login fails with invalid password."""
    login_page.goto()
    login_page.login(STANDARD_USER, "wrong_password")
    login_page.expect_error("Username and password do not match")


@pytest.mark.regression
def test_login_fails_with_locked_out_user(login_page):
    """LOGIN-03: Login fails with locked-out user."""
    login_page.goto()
    login_page.login("locked_out_user", PASSWORD)
    login_page.expect_error("locked out")


@pytest.mark.regression
def test_login_fails_with_empty_fields(login_page):
    """LOGIN-04: Login fails with empty fields."""
    login_page.goto()
    login_page.login("", "")
    login_page.expect_error("Username is required")
