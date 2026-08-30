# ==========================================
# SOLUTION: Solo Challenge 2 (test_challenge_hybrid.py)
# ==========================================
from playwright.sync_api import expect


def test_ultimate_hybrid_challenge(page):
    # 1. POST Request to create a new post
    response = page.request.post(
        "https://jsonplaceholder.typicode.com/posts",
        data={
            "title": "My QA Automation Post",
            "body": "Playwright is awesome!",
            "userId": 1
        }
    )
    
    # Assert status is 201 (Created)
    assert response.status == 201
    # Alternatively using expect: expect(response).to_be_ok()
    
    print(f"\nPost created successfully with ID: {response.json()['id']}")

    # 2. UI Navigation & Login
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    
    # 3. Final Assertion
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

# [INSTRUCTOR NOTE]: Remind students they don't need code to generate the trace here.
# They just need to run it in the terminal using:
# pytest tests/test_challenge_hybrid.py --tracing=retain-on-failure