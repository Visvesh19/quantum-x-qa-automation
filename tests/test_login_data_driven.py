
import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        (
            "invalid_user",
            "wrong_password",
            "Username and password do not match",
        ),
        (
            "locked_out_user",
            "secret_sauce",
            "Sorry, this user has been locked out",
        ),
        (
            "",
            "secret_sauce",
            "Username is required",
        ),
        (
            "standard_user",
            "",
            "Password is required",
        ),
        (
            "",
            "",
            "Username is required",
        ),
    ],
    ids=[
        "invalid-credentials",
        "locked-out-user",
        "empty-username",
        "empty-password",
        "both-fields-empty",
    ],
)
def test_invalid_login_scenarios(
    login_page, username, password, expected_error
):
    login_page.login(username, password)

    expect(login_page.error_message).to_contain_text(
        expected_error
    )
