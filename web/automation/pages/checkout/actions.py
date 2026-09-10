"""CheckoutPage — user actions (the 'Actions' partial)."""
from pages.checkout.map import CheckoutPageMap


class CheckoutPageActions(CheckoutPageMap):
    def fill_info(self, first_name: str, last_name: str, zip_code: str):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.zip_code.fill(zip_code)

    def submit_info(self):
        self.continue_button.click()

    def cancel(self):
        self.cancel_button.click()

    def finish(self):
        self.finish_button.click()
