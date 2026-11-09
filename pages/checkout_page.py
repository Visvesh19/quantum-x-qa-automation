
from playwright.sync_api import Page, expect


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.postal_code = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")

    def enter_customer_details(
        self, first_name: str, last_name: str, postal_code: str
    ):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)
        self.continue_button.click()

    def verify_order_summary(self):
        expect(self.page.locator(".title")).to_have_text(
            "Checkout: Overview"
        )

    def finish_order(self):
        self.finish_button.click()

    def verify_order_confirmation(self):
        expect(self.page.locator(".title")).to_have_text(
            "Checkout: Complete!"
        )
        expect(
            self.page.locator(".complete-header")
        ).to_have_text("Thank you for your order!")
