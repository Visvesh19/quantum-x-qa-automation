
import pytest
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    """Provide a reusable LoginPage for each test."""
    login = LoginPage(page)
    login.open()
    return login
