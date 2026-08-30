import time

from selenium import webdriver
from selenium.webdriver.common.by import By  # Required to use By.ID

driver = webdriver.Chrome()
# Going directly to a login form
driver.get("https://the-internet.herokuapp.com/login")

# 1. Finding the elements using their ID (Found via Right-Click -> Inspect)
username_box = driver.find_element(By.ID, "username")
password_box = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.CLASS_NAME, "radius") # Sometimes IDs aren't available!

# 2. Interacting (The Robot types)
print("Typing credentials...")
username_box.send_keys("tomsmith")
password_box.send_keys("SuperSecretPassword!")

time.sleep(2) # Pausing just for the live demo effect

# 3. Clicking
print("Clicking login...")
login_button.click()
time.sleep(2)

driver.quit()