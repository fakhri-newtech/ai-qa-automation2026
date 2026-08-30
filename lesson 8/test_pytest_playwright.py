
def test_jsonplaceholder_get_request(page):
    get_response = page.request.get("https://jsonplaceholder.typicode.com/posts/1")
    
    # Assert HTTP status is 200 OK
    assert get_response.status == 200
    
    data = get_response.json()
    assert data["id"] == 1
    assert "title" in data
    print("GET test passed successfully!")

def test_jsonplaceholder_post_request(page):
    url = "https://jsonplaceholder.typicode.com/posts"
    post_response = page.request.post(
        url, 
        data={
            "title": "Playwright with Pytest",
            "body": "Seamless integration between API and test runner",
            "userId": 100
        }
    )
    
    # Assert resource was successfully created (201)
    assert post_response.status == 201
    
    data = post_response.json()
    assert data["title"] == "Playwright with Pytest"
    assert data["userId"] == 100
    print("POST test passed successfully!")