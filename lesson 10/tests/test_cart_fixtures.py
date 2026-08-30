# ==========================================
# FILE: tests/test_cart_fixture.py
# ==========================================
from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage

# 1. We request 'logged_in_page' instead of the default 'page'
def test_add_item_with_fixture(logged_in_page: Page):
    
    # 2. We skip Login entirely! We start directly on the Inventory Page
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.add_backpack()
    
    # 3. Final assertion
    expect(logged_in_page.locator(".shopping_cart_link")).to_be_visible()


# ==========================================
# 🧠 INSTRUCTOR NOTES: Code Breakdown & Demo
# ==========================================
# 1. `def test_add_item_with_fixture(logged_in_page: Page):`
#    Notice there is ZERO import statement for `logged_in_page`! 
#    Pytest automatically scans `conftest.py` in the root folder, finds 
#    the matching fixture name, and executes the setup (login) for us.
#
# 2. `InventoryPage(logged_in_page)`:
#    Since our fixture used `yield page`, the `logged_in_page` variable IS 
#    exactly the Playwright Page object. We pass it right into our POM class.
#
# 3. INSTRUCTOR DEMO (Proving pytest.ini works):
#    Tell the students: "Let's test our safety net from the last slide!"
#    Intentionally BREAK the test by changing line 15 to:
#    `expect(logged_in_page.locator(".wrong_link")).to_be_visible(timeout=2000)`
#    
#    Click the VS Code green play button. Show the students how:
#       - The browser actually opens (because of `--headed` in .ini).
#       - The test fails safely.
#       - A "test-results" folder magically appears containing the screenshot 
#         and trace—with ZERO manual try/finally blocks in our Python code!
#    
#    (Don't forget to change the code back to `.shopping_cart_link` after the demo!)