import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Initialize the browser and create a new page context
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    
    # --- MODERN LOCATORS & ACTIONS ---
    # Notice we do NOT use sleep() or explicit waits before these actions.
    # Playwright's Auto-Waiting ensures the inputs are attached and visible before typing.
    
    print("Filling in username...")
    # .fill() automatically clears any placeholder text before typing our string
    page.locator("#user-name").fill("standard_user")
    
    print("Filling in password...")
    page.locator("#password").fill("secret_sauce")
    
    print("Clicking the login button...")
    # Playwright waits for the button to become clickable, then executes a native mouse click
    page.locator("#login-button").click()
    
    print("Login sequence executed successfully with zero manual waits!")
    
    # Pausing for 2 seconds purely for educational purposes so students can see the logged-in state
    time.sleep(2) 
    
    # Clean teardown
    browser.close()