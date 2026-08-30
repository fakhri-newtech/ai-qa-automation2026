from playwright.sync_api import sync_playwright, expect


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 1. GET Request & Assertions
    get_response = page.request.get("https://jsonplaceholder.typicode.com/posts/1")
    print(f"GET Status Code: {get_response.status}")
    
    # Assert that the API response was successful (HTTP 2xx)
    expect(get_response).to_be_ok()
    
    parsed_get_data = get_response.json()
    # Python standard assert for response content
    assert parsed_get_data["id"] == 1, "Error: Post ID mismatch!"
    print(f"Retrieved Title: {parsed_get_data['title']}\n")

    # 2. POST Request & Assertions
    url = "https://jsonplaceholder.typicode.com/posts"
    post_response = page.request.post(
        url, 
        data={
            "title": "Playwright is cool",
            "body": "I used playwright it is so much better than selenium",
            "userId": 100
        }
    )

    print(f"POST Status Code: {post_response.status}")
    # Assert HTTP 201 Created status code
    assert post_response.status == 201, "Error: Resource creation failed!"

    parsed_post_data = post_response.json()
    assert parsed_post_data["title"] == "Playwright is cool"
    
    print(f"ID is: {parsed_post_data['id']}")
    print(f"TITLE is: {parsed_post_data['title']}")

    browser.close()