"""CheckoutPage — assertions (the 'Asserts' partial)."""
from playwright.sync_api import expect
from pages.checkout.map import CheckoutPageMap


class CheckoutPageAsserts(CheckoutPageMap):
    def expect_error(self, text: str):
        expect(self.error_message).to_contain_text(text)

    def expect_confirmation(self):
        expect(self.confirmation_header).to_have_text("Thank you for your order!")

    def expect_total_visible(self):
        expect(self.total).to_be_visible()
