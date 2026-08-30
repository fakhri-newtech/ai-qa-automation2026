import pytest

def calculate_discount(user_type, cart_total):
    if user_type == "VIP":
        return cart_total * 0.80  # 20% off
    return cart_total

# Testing multiple scenarios in a single block of code
@pytest.mark.parametrize("user_type, cart_total, expected_total", [
    ("VIP", 100, 80),      # VIP gets 20% off
    ("Regular", 100, 100), # Regular pays full price
    ("VIP", 50, 40)        # VIP gets 20% off a smaller cart
])
def test_checkout_discounts(user_type, cart_total, expected_total):
    # 1. Execute the action
    final_price = calculate_discount(user_type, cart_total)
    
    # 2. Assert the result
    assert final_price == expected_total