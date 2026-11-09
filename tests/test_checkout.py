
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout_workflow(page, login_page):
    """
    Validate the complete Sauce Demo shopping workflow:
    1. Login
    2. Add product to cart
    3. Verify cart
    4. Enter customer details
    5. Validate checkout financial amounts
    6. Complete order
    7. Verify order confirmation
    """

    # Step 1: Login
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Add product to cart
    inventory = InventoryPage(page)
    inventory.verify_inventory_page()
    inventory.add_product_to_cart("Sauce Labs Backpack")
    inventory.verify_cart_count(1)

    # Step 3: Open cart
    inventory.open_cart()

    cart = CartPage(page)
    cart.verify_cart_page()
    cart.verify_product_in_cart("Sauce Labs Backpack")
    cart.verify_cart_quantity(1)

    # Step 4: Proceed to checkout
    cart.proceed_to_checkout()

    checkout = CheckoutPage(page)

    # Step 5: Enter customer details
    checkout.enter_customer_details(
        first_name="Test",
        last_name="Customer",
        postal_code="600001"
    )

    # Step 6: Verify checkout overview
    checkout.verify_order_summary()

    # Step 7: Validate subtotal, tax and total
    checkout.verify_checkout_amounts()

    # Step 8: Complete order
    checkout.finish_order()

    # Step 9: Verify order confirmation
    checkout.verify_order_confirmation()
