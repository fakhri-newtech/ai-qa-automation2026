# ==========================================
# SOLUTION: Solo Challenge 1 (test_challenge_assertions.py)
# ==========================================
from playwright.sync_api import expect


def test_saucedemo_challenge_assertions(page):
    page.goto("https://www.saucedemo.com/")
    
    # Login
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    
    # 1. Assert URL changed to inventory.html
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    # 2. Assert the "Products" title is visible
    products_title = page.locator(".title")
    expect(products_title).to_be_visible()
    expect(products_title).to_have_text("Products")
    
    # 3. Assert the shopping cart badge is NOT visible yet (cart is empty)
    cart_badge = page.locator(".shopping_cart_badge")
    expect(cart_badge).not_to_be_visible()