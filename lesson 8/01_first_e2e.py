from playwright.sync_api import sync_playwright

# The 'with' statement ensures browser resources are cleanly allocated and deallocated
with sync_playwright() as p:
    # 1. Launch the Chromium browser. 
    # headless=False opens a physical browser window so we can watch the test execute.
    browser = p.chromium.launch(headless=False)
    
    # 2. Create a new isolated context/tab. This is where our test runs safely.
    page = browser.new_page()
    
    # 3. Command the browser to navigate to the target E2E URL.
    print("Navigating to SauceDemo...")
    page.goto("https://www.saucedemo.com/")
    
    # 4. Fetch the page title natively to verify navigation was successful.
    actual_title = page.title()
    print(f"Success! The page title loaded is: {actual_title}")
    
    # 5. Clean teardown - close the browser to free up system memory.
    browser.close()