# ==========================================
# SNIPPET 3: Trace Viewer (test_tracing.py)
# ==========================================
from playwright.sync_api import expect, sync_playwright


def test_trace_viewer():
    # [INSTRUCTOR NOTE]: We write this manually (without the page fixture) to see how tracing starts/stops under the hood.
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        
        # [INSTRUCTOR NOTE]: The crucial step - start recording before opening the page!
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        
        page.goto("https://www.saucedemo.com/")
        page.locator("#user-name").fill("standard_user")
        
        # [INSTRUCTOR NOTE]: We intentionally use a wrong password to force a failure.
        page.locator("#password").fill("wrong_password")  
        page.locator("#login-button").click()
        
        # [INSTRUCTOR NOTE]: This assertion WILL fail. The timeout is short (2s) to speed up the failure.
        expect(page.locator(".title")).to_have_text("Products", timeout=2000)
        
        # [INSTRUCTOR NOTE]: Stop recording and save the zip file.
        context.tracing.stop(path="trace.zip")
        browser.close()
        
        # [INSTRUCTOR NOTE]: Tell students: Do NOT unzip the file. 
        # Open terminal and run: playwright show-trace trace.zip