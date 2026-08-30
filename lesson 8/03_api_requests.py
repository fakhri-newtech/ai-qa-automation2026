from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser context - this time we will focus on the native API engine
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # ==========================================
    # 1. SENDING A 'GET' REQUEST
    # ==========================================
    print("--- Testing API GET Request ---")
    
    # page.request natively handles backend HTTP requests without the external 'requests' library
    get_response = page.request.get("https://jsonplaceholder.typicode.com/posts/1")
    
    # Verify the HTTP status code (e.g., 200 OK)
    print(f"Status Code: {get_response.status}")
    
    # Playwright dynamically parses the JSON response body into a Python dictionary
    parsed_get_data = get_response.json()
    print(f"Retrieved Title: {parsed_get_data['title']}\n")
    
    
    # ==========================================
    # 2. SENDING A 'POST' REQUEST
    # ==========================================
    print("--- Testing API POST Request ---")
    
    # Sending a POST request with a JSON payload in a single, elegant command
    post_response = page.request.post(
        "https://jsonplaceholder.typicode.com/posts",
        data={
            "title": "Playwright is awesome",
            "body": "Testing native backend API contexts directly from UI tests.",
            "userId": 99
        }
    )
    
    # Verify the HTTP status code (e.g., 201 Created)
    print(f"Status Code: {post_response.status}")
    
    # Verify the backend server processed and returned our specific test data
    parsed_post_data = post_response.json()
    print(f"Created ID from Server: {parsed_post_data['id']}")
    print(f"Created Title from Server: {parsed_post_data['title']}")
    
    # Clean teardown
    browser.close()