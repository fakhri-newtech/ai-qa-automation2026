# ==========================================
# FILE: tests/test_e2e_purchase.py
# ==========================================
from playwright.sync_api import Page, expect

# 1. Import BOTH custom Page Objects
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_item_to_cart(page: Page):
    # 2. Instantiate both objects, sharing the same 'page' fixture
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    
    # 3. Execute the seamless business flow
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page.add_backpack()
    
    # 4. Spaced Repetition: Final test-level assertion
    expect(page.locator(".shopping_cart_link")).to_be_visible()


# ==========================================
# 🧠 INSTRUCTOR NOTES: Code Breakdown & Review
# (Explain this immediately after executing the test successfully)
# ==========================================
# 1. Sharing the `page` fixture:
#    Point out that we passed `(page)` into BOTH `LoginPage` and `InventoryPage`. 
#    Why? Because there is only ONE browser window open. We are simply handing 
#    the "remote control" of that single browser from the Login Page to the 
#    Inventory Page as the user navigates through the site.
#
# 2. The Power of Readability:
#    Tell the students: "Read lines 16 to 19 out loud. 'Navigate, login, 
#    add backpack'. You don't need to be a programmer to understand this test. 
#    This is what senior engineers aim for: Code that documents itself."
#
# 3. Maintenance Isolation:
#    Ask them: "If SauceDemo completely redesigns their website tomorrow and 
#    changes every single ID and CSS class, do we need to touch THIS file?"
#    Answer: "NO! We only update the files in the `pages/` directory. This 
#    test file remains untouched forever. That is the magic of POM."
#
# 4. Logical Verification Check:
#    The `add_backpack()` method already contains an `expect` that waits for 
#    the cart badge to equal "1". By the time the code reaches line 22, we 
#    are mathematically certain the UI has updated, making the final assertion 
#    stable and flake-free.