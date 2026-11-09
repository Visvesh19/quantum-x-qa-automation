
import pytest
from playwright.sync_api import expect

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.parametrize(
    "first_name,last_name,postal_code,expected_error",
    [
        ("", "Customer", "600001",
         "Error: First Name is required"),
        ("Test", "", "600001",
         "Error: Last Name is required"),
        ("Test", "Customer", "",
         "Error: Postal Code is required"),
    ],
    ids=[
        "missing-first-name",
        "missing-last-name",
        "missing-postal-code",
    ],
)
def test_checkout_required_fields(
    page,
    login_page,
    first_name,
    last_name,
    postal_code,
    expected_error,
):
    # Login
    login_page.login("standard_user", "secret_sauce")

    # Add product
    inventory = InventoryPage(page)
    inventory.add_product_to_cart("Sauce Labs Backpack")
    inventory.open_cart()

    # Proceed to checkout
    cart = CartPage(page)
    cart.proceed_to_checkout()

    # Enter test data
    checkout = CheckoutPage(page)
    checkout.enter_customer_details(
        first_name,
        last_name,
        postal_code,
    )

    # Verify validation error
    error_message = page.locator(
        "[data-test='error']"
    )
    expect(error_message).to_have_text(expected_error)

    # Verify checkout did not proceed
    expect(page).to_have_url(
        "https://www.saucedemo.com/checkout-step-one.html"
    )
