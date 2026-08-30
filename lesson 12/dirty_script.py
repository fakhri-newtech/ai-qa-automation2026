import time
from playwright.sync_api import sync_playwright

def test_buy_item_legacy():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.saucedemo.com")
        page.locator("#user-name").type("standard_user")
        page.locator("#password").type("secret_sauce")
        page.locator(".btn_action").click()
        
        time.sleep(3)
        
        page.locator(".inventory_item:nth-child(1) button").click()
        time.sleep(1)
        
        page.locator(".shopping_cart_link").click()
        
        assert page.locator(".inventory_item_name").text_content() == "Sauce Labs Backpack"
        
        browser.close()