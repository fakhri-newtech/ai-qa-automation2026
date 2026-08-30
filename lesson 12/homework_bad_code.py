import time
from playwright.sync_api import sync_playwright

def test_menu_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        
        time.sleep(2) 

        page.click("//button[text()='Open Menu']")
        
        time.sleep(1) 

        page.click("#about_sidebar_link")
        
        assert page.url == "https://saucelabs.com/"
        
        browser.close()