# ==========================================
# FILE: pages/inventory_page.py
# ==========================================
from playwright.sync_api import Page, expect

class InventoryPage:
    
    def __init__(self, page: Page):
        self.page = page
        # Locating the specific Add to Cart button for the Sauce Labs Backpack
        self.add_backpack_btn = page.locator("#add-to-cart-sauce-labs-backpack")
        # Locating the red badge that appears on the cart icon
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_backpack(self):
        self.add_backpack_btn.click()
        
        # Spaced Repetition: Asserting inside the Page Object
        expect(self.cart_badge).to_have_text("1", timeout=3000)


# ==========================================
# 🧠 INSTRUCTOR NOTES: Code Breakdown & Review
# (Explain this while reviewing the solution with the class)
# ==========================================
# 1. `self.add_backpack_btn = page.locator("#add-to-cart-sauce-labs-backpack")`:
#    Ask the class: "Who used a different locator?"
#    Explain that IDs are the most stable, but `[data-test='...']` is also 
#    a perfect answer if any student used it.
#
# 2. `self.cart_badge = page.locator(".shopping_cart_badge")`:
#    Remind them that in CSS, a dot (`.`) represents a class. The cart badge 
#    doesn't have an ID, so we rely on the class name.
#
# 3. `expect(self.cart_badge).to_have_text("1")`:
#    Why do we put the expect here instead of in the test file?
#    Explain: "Because clicking 'Add to Cart' should ALWAYS result in the 
#    cart badge updating. By asserting it right inside the Page Object, 
#    we ensure that every test that calls `add_backpack()` automatically 
#    verifies the UI responded correctly. We build trust into our actions."
#
# 4. Logical Verification Check:
#    The `.shopping_cart_badge` element does NOT exist in the DOM until 
#    an item is added. Playwright's auto-waiting handles this perfectly. 
#    When `.click()` happens, the DOM updates, and `.to_have_text()` 
#    waits up to 3 seconds for the element to appear and contain "1".