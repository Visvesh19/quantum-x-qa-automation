
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout_workflow(page, login_page):
    """
    QUANTUM-X: End-to-End Checkout and Price Validation

    Validates:
    - Successful login
    - Product inventory
    - Inventory, cart and checkout price consistency
    - Cart product and quantity
    - Checkout subtotal, tax and grand total
    - Successful order completion
    """

    product_name = "Sauce Labs Backpack"

    # Step 1: Login
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Verify inventory and capture price
    inventory = InventoryPage(page)
    inventory.verify_inventory_page()

    inventory_price = inventory.get_product_price(
        product_name
    )

    # Step 3: Add product to cart
    inventory.add_product_to_cart(product_name)
    inventory.verify_cart_count(1)
    inventory.open_cart()

    # Step 4: Verify cart details and capture price
    cart = CartPage(page)
    cart.verify_cart_page()
    cart.verify_product_in_cart(product_name)
    cart.verify_cart_quantity(1)

    cart_price = cart.get_product_price(product_name)

    # Step 5: Compare inventory and cart prices
    assert inventory_price == cart_price, (
        f"Inventory/Cart price mismatch: "
        f"Inventory={inventory_price}, "
        f"Cart={cart_price}"
    )

    # Step 6: Proceed to checkout
    cart.proceed_to_checkout()

    checkout = CheckoutPage(page)

    # Step 7: Enter customer details
    checkout.enter_customer_details(
        first_name="Test",
        last_name="Customer",
        postal_code="600001"
    )

    # Step 8: Verify checkout overview
    checkout.verify_order_summary()

    # Step 9: Capture checkout product price
    checkout_price = checkout.parse_amount(
        checkout.cart_items.locator(
            ".inventory_item_price"
        ).inner_text()
    )

    # Step 10: Compare all three prices
    assert inventory_price == cart_price == checkout_price, (
        f"Product price mismatch: "
        f"Inventory={inventory_price}, "
        f"Cart={cart_price}, "
        f"Checkout={checkout_price}"
    )

    # Step 11: Verify subtotal, tax and grand total
    checkout.verify_checkout_amounts()

    # Step 12: Complete order
    checkout.finish_order()

    # Step 13: Verify confirmation
    checkout.verify_order_confirmation()
