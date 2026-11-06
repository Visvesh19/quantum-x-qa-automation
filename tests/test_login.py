
from playwright.sync_api import Page, expect


def test_valid_login(page: Page, login_page):
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )
    expect(page.locator(".title")).to_have_text("Products")


def test_invalid_login(login_page):
    login_page.login("invalid_user", "wrong_password")

    expect(login_page.error_message).to_contain_text(
        "Username and password do not match"
    )
