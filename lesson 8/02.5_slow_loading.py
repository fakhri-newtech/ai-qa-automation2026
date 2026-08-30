import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    print("Navigating to dynamic loading page...")
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
    
    print("Clicking start...")
    page.locator("#start button").click()
    print("Waiting for the text to load...")
    
    # ==========================================
    # 🪄 THE AUTO-WAIT MAGIC 🪄
    # ==========================================
    # In Selenium, you HAD to write: driver.implicitly_wait(10)
    # If you forgot it, Selenium would crash right here with NoSuchElementException.
    # Playwright automatically polls the DOM and waits for the element to attach and be visible!
    
    finish_text = page.locator("#finish").inner_text()
    
    print(f"Success! Found it: {finish_text}")
    
    time.sleep(2)
    browser.close()