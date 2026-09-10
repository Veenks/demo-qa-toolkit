"""CheckoutPage — element locators (the 'Map' partial).

Covers all three checkout steps (info, overview, complete) since they're
a single conceptual flow. If this grows too large, split into
checkout_info / checkout_overview / checkout_complete sub-packages
following the same Map/Actions/Asserts pattern.
"""
from playwright.sync_api import Page


class CheckoutPageMap:
    INFO_URL = "https://www.saucedemo.com/checkout-step-one.html"
    OVERVIEW_URL = "https://www.saucedemo.com/checkout-step-two.html"
    COMPLETE_URL = "https://www.saucedemo.com/checkout-complete.html"

    def __init__(self, page: Page):
        self.page = page
        # Step one — info
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.zip_code = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.cancel_button = page.locator("#cancel")
        self.error_message = page.locator("[data-test='error']")
        # Step two — overview
        self.item_total = page.locator(".summary_subtotal_label")
        self.tax = page.locator(".summary_tax_label")
        self.total = page.locator(".summary_total_label")
        self.finish_button = page.locator("#finish")
        # Step three — complete
        self.confirmation_header = page.locator(".complete-header")
