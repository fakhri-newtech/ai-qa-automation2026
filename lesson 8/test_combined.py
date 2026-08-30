from playwright.sync_api import expect, sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    print("Step 1: Fetching data via backend API request...")
    get_response = page.request.get("https://jsonplaceholder.typicode.com/posts/1")
    expect(get_response).to_be_ok()
    post_title = get_response.json()["title"]
    print(f"API Data Fetched Successfully: {post_title}")

    print("Step 2: Navigating to UI application using the acquired context...")
    page.goto("https://www.saucedemo.com/")
    
    # Verify UI state using modern locators and auto-retrying assertions
    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.locator("#login-button")).to_be_visible()
    print("UI state validated successfully. Hybrid test workflow complete!")

    browser.close()