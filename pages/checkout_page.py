
from decimal import Decimal, ROUND_HALF_UP
from playwright.sync_api import Page, expect


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

        self.first_name = page.locator(
            "[data-test='firstName']"
        )
        self.last_name = page.locator(
            "[data-test='lastName']"
        )
        self.postal_code = page.locator(
            "[data-test='postalCode']"
        )
        self.continue_button = page.locator(
            "[data-test='continue']"
        )
        self.finish_button = page.locator(
            "[data-test='finish']"
        )

        self.cart_items = page.locator(".cart_item")
        self.subtotal = page.locator(
            "[data-test='subtotal-label']"
        )
        self.tax = page.locator(
            "[data-test='tax-label']"
        )
        self.total = page.locator(
            "[data-test='total-label']"
        )

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

    @staticmethod
    def parse_amount(text: str) -> Decimal:
        return Decimal(text.split("$")[-1].strip())

    def verify_checkout_amounts(self):
        expected_subtotal = Decimal("0.00")

        for item in self.cart_items.all():
            price = self.parse_amount(
                item.locator(
                    ".inventory_item_price"
                ).inner_text()
            )
            quantity = int(
                item.locator(
                    ".cart_quantity"
                ).inner_text()
            )
            expected_subtotal += price * quantity

        actual_subtotal = self.parse_amount(
            self.subtotal.inner_text()
        )
        actual_tax = self.parse_amount(
            self.tax.inner_text()
        )
        actual_total = self.parse_amount(
            self.total.inner_text()
        )

        expected_tax = (
            expected_subtotal * Decimal("0.08")
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )

        expected_total = expected_subtotal + expected_tax

        assert actual_subtotal == expected_subtotal, (
            f"Subtotal mismatch: expected {expected_subtotal}, "
            f"actual {actual_subtotal}"
        )

        assert actual_tax == expected_tax, (
            f"Tax mismatch: expected {expected_tax}, "
            f"actual {actual_tax}"
        )

        assert actual_total == expected_total, (
            f"Total mismatch: expected {expected_total}, "
            f"actual {actual_total}"
        )

    def finish_order(self):
        self.finish_button.click()

    def verify_order_confirmation(self):
        expect(self.page.locator(".title")).to_have_text(
            "Checkout: Complete!"
        )
        expect(
            self.page.locator(".complete-header")
        ).to_have_text(
            "Thank you for your order!"
        )
