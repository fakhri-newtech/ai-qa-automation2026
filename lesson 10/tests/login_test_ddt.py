# ==========================================
# FILE: tests/test_login_ddt.py
# ==========================================
import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

# 1. Decorate the test to feed it multiple datasets
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("visual_user", "secret_sauce")
])
def test_multiple_users_login(page: Page, username, password):
    
    # 2. Revert to standard 'page' fixture so we can control the login
    login_page = LoginPage(page)
    login_page.navigate()
    
    # 3. Pass the dynamic variables into our POM method
    login_page.login(username, password)
    
    # 4. Assert the login was successful for each user
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


# ==========================================
# 🧠 INSTRUCTOR NOTES: Code Breakdown & New Keywords
# (Explain these concepts immediately after typing)
# ==========================================
# 1. `import pytest`:
#    Unlike our previous tests, we MUST import pytest here because we are 
#    using one of its specific features (the parametrize decorator).
#
# 2. `@pytest.mark.parametrize("username, password", [ ... ])`:
#    - **The String:** `"username, password"` tells Pytest the exact names 
#      of the variables we want to inject into our test function.
#    - **The List of Tuples:** `[ ("user1", "pass1"), ("user2", "pass2") ]` 
#      contains the actual data. Each tuple represents ONE complete test run.
#
# 3. `def test_multiple_users_login(page: Page, username, password):`
#    Notice that we added `username` and `password` as arguments next to `page`. 
#    Pytest takes the data from the decorator and magically pushes it into 
#    these variables.
#
# 4. Logical Verification & Execution Check:
#    Run this file using the VS Code play button or terminal. 
#    Point out to the students that the browser opens and closes THREE TIMES.
#    Pytest treats this as 3 completely separate, isolated tests, ensuring 
#    that if `problem_user` fails, `visual_user` will still execute!