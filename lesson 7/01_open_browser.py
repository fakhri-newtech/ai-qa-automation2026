import time

from selenium import webdriver

print("Starting the browser...")
# 1. Open Chrome
driver = webdriver.Chrome()

# 2. Navigate to a website
driver.get("https://the-internet.herokuapp.com/")

# 3. Read some data to prove we are there
print(f"I am currently on: {driver.title}")

# Just pausing for 3 seconds so the students can actually see it before it closes
time.sleep(3) 

# 4. ALWAYS close the browser
print("Closing the browser...")
driver.quit()