def test_api_status_success():
    # Simulating a successful server response
    status_code = 200
    
    # If this is True, Pytest stays quiet and passes the test
    assert status_code == 200

def test_api_status_failure():
    # Simulating a server crash
    status_code = 500
    
    # If this is False, Pytest crashes the test and prints the custom message
    assert status_code == 200, f"Test Failed: Expected 200 but got {status_code}"