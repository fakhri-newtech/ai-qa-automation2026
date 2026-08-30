from selenium import webdriver
from selenium.webdriver.common.by import By


def test_successful_login():
    # 1. Setup
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    # 2. Act
    # Find elements
    user_box = driver.find_element(By.ID, "user-name")
    pass_box = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-button")
    
    # Interact
    user_box.send_keys("standard_user")
    pass_box.send_keys("secret_sauce")
    login_btn.click()
    
    # 3. Assert (Did it work?)
    # If login works, the URL changes to the inventory page
    assert "inventory.html" in driver.current_url, "Login failed, URL did not change!"
    
    # 4. Teardown (Cleanup)
    driver.quit()