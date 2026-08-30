# ==========================================
# FILE: tests/test_login_pom.py
# ==========================================
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_valid_login_pom(page: Page):
    login_page = LoginPage(page)
    
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


# ==========================================
# 🧠 INSTRUCTOR NOTES: Code Breakdown & New Keywords
# (Explain these concepts to the students immediately after typing)
# ==========================================
# 1. `from pages.login_page import LoginPage`:
#    This is a custom Python import. `pages` is the folder, `login_page` 
#    is the Python file, and `LoginPage` is the exact name of the Class.
#    (Tip: If VS Code underlines this in yellow, tell students not to worry;
#    running `pytest` from the root folder will find it automatically).
#
# 2. `login_page = LoginPage(page)`:
#    This is Object Instantiation. We tell Python: "Take the blueprint 
#    (LoginPage) and build a real object out of it." 
#    We pass the Pytest `page` fixture into it so the Page Object knows 
#    which browser to control.
#
# 3. `login_page.navigate()` and `login_page.login(...)`:
#    Look at how readable the test is now! No locators cluttering the test.
#
# 4. Control Flow Verification Check:
#    Because we use the Pytest `page` fixture, Pytest automatically handles 
#    the teardown. If the final `expect` fails, the browser safely closes.