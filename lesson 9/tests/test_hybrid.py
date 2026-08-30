# ==========================================
# SNIPPET 5: Hybrid Tests (test_hybrid.py)
# ==========================================
from playwright.sync_api import expect


def test_api_ui_hybrid(page):
    # [INSTRUCTOR NOTE]: Step 1 - Use API to fetch data or setup state instantly (Milliseconds).
    print("\n--- Step 1: API Request ---")
    response = page.request.get("https://jsonplaceholder.typicode.com/posts/1")
    
    # [INSTRUCTOR NOTE]: Assert the API request was successful (200 OK).
    expect(response).to_be_ok()
    api_title = response.json()["title"]
    print(f"API Data Fetched: {api_title}")

    # [INSTRUCTOR NOTE]: Step 2 - Switch to UI in the same browser context for visual assertions.
    print("--- Step 2: UI Validation ---")
    page.goto("https://www.saucedemo.com/")
    
    # [INSTRUCTOR NOTE]: Assert the UI state.
    expect(page).to_have_title("Swag Labs")
    expect(page.locator("#login-button")).to_be_visible()
    print("Hybrid test completed successfully!")
    
    # [INSTRUCTOR NOTE]: Remind students this shares the same browser context, 
    # so cookies/tokens set via API will apply to the UI automatically!