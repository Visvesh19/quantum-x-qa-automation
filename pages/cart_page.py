
from playwright.sync_api import Page, expect


class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator(
            "[data-test='checkout']"
        )

    def verify_cart_page(self):
        expect(self.page.locator(".title")).to_have_text(
            "Your Cart"
        )

    def verify_product_in_cart(self, product_name: str):
        expect(
            self.cart_items.locator(".inventory_item_name")
        ).to_contain_text([product_name])

    def verify_cart_quantity(self, expected_quantity: int):
        expect(
            self.page.locator(".cart_quantity")
        ).to_have_text(str(expected_quantity))

    def proceed_to_checkout(self):
        self.checkout_button.click()
