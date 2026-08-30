import pytest

# 1. The Setup (The Fixture)
@pytest.fixture
def mock_admin_user():
    print("\n[Setting up mock user data...]") # Proves to students this runs first
    return {
        "username": "admin_fakhri",
        "role": "admin",
        "is_active": True
    }

# 2. The Test (Injecting the Fixture)
def test_admin_has_access(mock_admin_user):
    # Pytest automatically passes the dictionary into this variable!
    assert mock_admin_user["role"] == "admin"
    assert mock_admin_user["is_active"] == True, "User should be active!"