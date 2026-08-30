# ==========================================
# SNIPPET 1: Smart Assertions (test_assertions.py)
# ==========================================
from playwright.sync_api import expect


def test_saucedemo_assertions(page):
    # [INSTRUCTOR NOTE]: First, we navigate to the page.
    page.goto("https://www.saucedemo.com/")
    
    # [INSTRUCTOR NOTE]: 1. Page Assertion - Check the page as a whole.
    expect(page).to_have_title("Swag Labs")
    
    # [INSTRUCTOR NOTE]: 2. Locator Assertion - Grab a specific element first.
    login_btn = page.locator("#login-button")
    
    # [INSTRUCTOR NOTE]: Make sure it is visible on the screen.
    expect(login_btn).to_be_visible()
    # [INSTRUCTOR NOTE]: Check its exact text/value.
    expect(login_btn).to_have_value("Login")
    
    # [INSTRUCTOR NOTE]: 3. Negative Assertion - How to check if something is NOT there.
    error_msg = page.locator("[data-test='error']")
    # [INSTRUCTOR NOTE]: We use not_ to assert the error is hidden initially.
    expect(error_msg).not_to_be_visible()

    
    # [INSTRUCTOR NOTE]: Tell students to run this using `pytest`. Notice how smooth it runs!