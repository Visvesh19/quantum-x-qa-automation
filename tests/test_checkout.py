
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout_workflow(page, login_page):
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_product_to_cart("Sauce Labs Backpack")
    inventory.verify_cart_count(1)
    inventory.open_cart()

    cart = CartPage(page)
    cart.verify_cart_page()
    cart.verify_product_in_cart("Sauce Labs Backpack")
    cart.proceed_to_checkout()

    checkout = CheckoutPage(page)
    checkout.enter_customer_details(
        "Test",
        "Customer",
        "600001"
    )

    checkout.verify_order_summary()
    checkout.finish_order()
    checkout.verify_order_confirmation()
