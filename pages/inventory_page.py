
from playwright.sync_api import Page, expect


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.products = page.locator(".inventory_item")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def verify_inventory_page(self):
        expect(self.page.locator(".title")).to_have_text(
            "Products"
        )

    def verify_products_displayed(self):
        expect(self.products).to_have_count(6)

    def add_product_to_cart(self, product_name: str):
        product = self.products.filter(
            has=self.page.locator(
                ".inventory_item_name",
                has_text=product_name
            )
        )
        product.get_by_role(
            "button", name="Add to cart"
        ).click()

    def verify_cart_count(self, expected_count: int):
        expect(self.cart_badge).to_have_text(
            str(expected_count)
        )

    def open_cart(self):
        self.cart_link.click()
