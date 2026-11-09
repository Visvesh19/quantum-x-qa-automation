
from pages.inventory_page import InventoryPage


def test_inventory_products_displayed(page, login_page):
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)

    inventory.verify_inventory_page()
    inventory.verify_products_displayed()


def test_add_product_to_cart(page, login_page):
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)

    inventory.add_product_to_cart("Sauce Labs Backpack")
    inventory.verify_cart_count(1)
