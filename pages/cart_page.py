
from decimal import Decimal
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
        product = self.cart_items.filter(
            has=self.page.locator(
                ".inventory_item_name",
                has_text=product_name
            )
        )
        expect(product).to_have_count(1)

    def verify_cart_quantity(self, expected_quantity: int):
        expect(
            self.page.locator(".cart_quantity")
        ).to_have_text(str(expected_quantity))

    def get_product_price(self, product_name: str) -> Decimal:
        product = self.cart_items.filter(
            has=self.page.locator(
                ".inventory_item_name",
                has_text=product_name
            )
        )

        expect(product).to_have_count(1)

        price_text = product.locator(
            ".inventory_item_price"
        ).inner_text()

        return Decimal(
            price_text.replace("$", "").strip()
        )

    def proceed_to_checkout(self):
        self.checkout_button.click()
