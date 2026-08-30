# ==========================================
# FILE: tests/test_invalid_login_ddt.py
# ==========================================
import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

# 1. Parameterize with 3 variables to link inputs with expected outcomes
@pytest.mark.parametrize("username, password, expected_error", [
    ("locked_out_user", "secret_sauce", "locked out"),
    ("standard_user", "wrong_password", "do not match"),
    ("", "", "Username is required")
])
def test_invalid_logins(page: Page, username, password, expected_error):
    
    # 2. Instantiate the POM
    login_page = LoginPage(page)
    login_page.navigate()
    
    # 3. Perform the dynamic action
    login_page.login(username, password)
    
    # 4. Assert the dynamic error message appears correctly
    expect(login_page.error_message).to_contain_text(expected_error)


# ==========================================
# 🧠 INSTRUCTOR NOTES: Code Breakdown & Review
# (Explain this while reviewing the solution with the class)
# ==========================================
# 1. Three Variables (`username, password, expected_error`):
#    Explain to the students: "Notice how we added a 3rd column to our data? 
#    This is best practice for DDT. You don't just parameterize the inputs; 
#    you MUST parameterize the expected results too. This way, the test knows 
#    exactly what success looks like for each specific scenario."
#
# 2. `expect(login_page.error_message).to_contain_text(expected_error)`:
#    - Ask the class: "Why did we use `to_contain_text` instead of `to_have_text`?"
#    - Explain: "SauceDemo's actual error message is very long (e.g., 'Epic sadface: 
#      Sorry, this user has been locked out.'). If developers change 'Epic sadface' 
#      to 'Error', our test breaks. By checking only for 'locked out' (the core 
#      business logic), our test becomes much more stable!"
#
# 3. Logical Verification Check:
#    When we run this, Pytest executes 3 tests. Even if the empty string test ("", "")
#    triggers a different behavior in the browser, the teardown is automatically 
#    handled by Pytest after every single iteration.