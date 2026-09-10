"""Shared pytest fixtures: page objects wired up and ready to use in tests."""
import pytest
from pages.login import LoginPage
from pages.inventory import InventoryPage
from pages.cart import CartPage
from pages.checkout import CheckoutPage

STANDARD_USER = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)


@pytest.fixture
def logged_in_page(login_page, inventory_page):
    """Starts every test already logged in as standard_user, on the inventory page."""
    login_page.goto()
    login_page.login(STANDARD_USER, PASSWORD)
    inventory_page.is_loaded()
    return inventory_page
