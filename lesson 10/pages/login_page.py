# ==========================================
# FILE: pages/login_page.py
# ==========================================
from playwright.sync_api import Page, expect


class LoginPage:
    
    # 1. Initialize the page and locators ONCE
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']") 

    # 2. Action: Navigate to the page
    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")
        # Spaced Repetition: Using expect to ensure the page is ready
        expect(self.login_button).to_be_visible(timeout=5000)

    # 3. Action: Perform the login
    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()


# class LoginPage:
# Explanation: This tells Python we are creating a blueprint for an object. 
# Instead of random scattered code, 
# everything related to the Login Page lives inside this blueprint.

# def __init__(self, page: Page):
# Explanation: This is the "constructor" or initialization method. 
# It runs automatically the exact moment we create a LoginPage object.

# Keyword self: In Python, self represents the object itself. 
# We use it to attach variables to the object (like self.username_input) 
# so they can be accessed anywhere else inside the class.

# Element page: Page: This is called a Type Hint. 
# By importing Page at the top and writing : Page, we tell VS Code that this variable is a 
# Playwright Page. This is what makes VS Code's autocomplete (IntelliSense) work so you can see 
# .locator() pop up when you type!

# expect(self.login_button).to_be_visible(...)
# Explanation: We are embedding our assertions directly into the page actions. 
# By putting this inside the navigate() method, we guarantee that any test calling this 
# method will automatically wait for the page to fully render before continuing.