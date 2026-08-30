# ==========================================
# SNIPPET 2: Screenshots (test_screenshots.py)
# ==========================================
def test_screenshots(page):
    # [INSTRUCTOR NOTE]: Setup the page state
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    
    # [INSTRUCTOR NOTE]: Element Screenshot - Target a specific locator and screenshot only that.
    page.locator(".login_box").screenshot(path="login_form.png")
    
    # [INSTRUCTOR NOTE]: Full Page Screenshot - Capture the entire browser view.
    page.screenshot(path="full_page.png")
    
    # [INSTRUCTOR NOTE]: Have students run this and check their project folder for the .png files!
