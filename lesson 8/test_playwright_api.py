from playwright.sync_api import sync_playwright

def test_jsonplaceholder_get():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        get_response = page.request.get("https://jsonplaceholder.typicode.com/posts/1")
        print(f"status code: {get_response.status}")
        
        assert get_response.status == 200, f"Expected 200, got {get_response.status}"

        parsed_get_data = get_response.json()
        print(f"Retrieved Title: {parsed_get_data['title']}\n")
        
        assert parsed_get_data["id"] == 1
        assert "title" in parsed_get_data

        browser.close()

def test_jsonplaceholder_post():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        url = "https://jsonplaceholder.typicode.com/posts"
        post_response = page.request.post(
            url, 
            data={
                "title": "Playwright is cool",
                "body": "I used playwright it is so much better than selenium",
                "userId": 100
            }
        )

        print(f"Status Code: {post_response.status}")
        
        assert post_response.status == 201, f"Expected 201, got {post_response.status}"

        parsed_post_data = post_response.json()
        print(f"ID is: {parsed_post_data['id']}")
        print(f"TITLE is: {parsed_post_data['title']}")

        assert parsed_post_data["title"] == "Playwright is cool"
        assert parsed_post_data["userId"] == 100

        browser.close()