import pytest


# A fake function simulating our app's login logic
def check_password_length(password):
    return len(password) >= 8

# Running ONE test function THREE times with different data
@pytest.mark.parametrize("test_password", [
    "123",           # Too short (Fails)
    "admin",         # Too short (Fails)
    "SuperSecret1!"  # Good length (Passes)
])
def test_password_security(test_password):
    # The assert will evaluate each password one by one
    is_secure = check_password_length(test_password)
    
    assert is_secure == True, f"Password '{test_password}' is too short!"