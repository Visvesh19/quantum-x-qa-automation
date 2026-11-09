
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_backpack_and_verify_cart(page, login_page):
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_product_to_cart("Sauce Labs Backpack")
    inventory.verify_cart_count(1)
    inventory.open_cart()

    cart = CartPage(page)
    cart.verify_cart_page()
    cart.verify_product_in_cart("Sauce Labs Backpack")
    cart.verify_cart_quantity(1)
