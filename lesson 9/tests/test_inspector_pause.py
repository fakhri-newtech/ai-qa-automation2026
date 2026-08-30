# ==========================================
# SNIPPET 4: Advanced Debugging (test_inspector_pause.py)
# ==========================================
def test_inspector_pause(page):
    page.goto("https://www.saucedemo.com/")
    
    # [INSTRUCTOR NOTE]: The magic pause button. 
    # This freezes the browser and opens the Playwright Inspector UI.
    page.pause()  
    
    # [INSTRUCTOR NOTE]: The code below won't execute until you click "Resume" in the Inspector.
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    
    # [INSTRUCTOR NOTE]: BIG WARNING! 
    # Never push page.pause() to GitHub. It will hang the CI/CD pipeline forever.
    # Tell students: Delete page.pause() and instead run the test using: pytest --debug