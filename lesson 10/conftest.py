# ==========================================
# FILE: conftest.py (Must be in the project root folder)
# ==========================================
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

# 1. Decorate the function to tell Pytest this is a Fixture
@pytest.fixture
def logged_in_page(page: Page):
    # ==========================================
    # --- SETUP PHASE (Executes BEFORE the test) ---
    # ==========================================
    print("\n[Setup]: Navigating and logging in...")
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    # 2. Pause the fixture and hand the browser to the test
    yield page  
    
    # ==========================================
    # --- TEARDOWN PHASE (Executes AFTER the test) ---
    # ==========================================
    print("\n[Teardown]: Test finished. Pytest will now close the browser.")


# ==========================================
# 🧠 INSTRUCTOR NOTES: Code Breakdown & New Keywords
# (Explain these concepts immediately after typing)
# ==========================================
# 1. File Location (`conftest.py`):
#    Emphasize that this file MUST be in the root directory. Pytest looks for 
#    this exact filename automatically. If they spell it `configtest.py`, 
#    it will fail!
#
# 2. `@pytest.fixture`:
#    This is called a "Decorator". It's a special label we put above a Python 
#    function to change its behavior. It tells Pytest: "This isn't a normal 
#    function; this is a setup tool that tests can request."
#
# 3. The `yield` Keyword (CRITICAL CONCEPT):
#    Ask the students: "Why didn't we use `return page`?"
#    Explain: "If we use `return`, the function ends immediately. Nothing 
#    after `return` will ever execute. `yield` is like a pause button. 
#    It hands the `page` to the test, waits for the test to finish, and 
#    then resumes running the code below it. This is how we guarantee 
#    our Teardown steps (like closing connections or printing logs) run!"
#
# 4. Logical Verification Check:
#    Even if the actual test fails and crashes, Pytest guarantees that the 
#    code AFTER the `yield` will still execute. This replaces the need 
#    for manual `try...finally` blocks in our test files!