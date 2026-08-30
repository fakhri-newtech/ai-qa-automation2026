import requests


def test_get_single_user():
    url = "https://reqres.in/api/users/2"
    response = requests.get(url)
    
    data = response.json()

    
    assert response.status_code == 200
    
    assert data["data"]["id"] == 2
    assert data["data"]["first_name"] == "Janet"

def test_create_new_user():
    url = "https://reqres.in/api/users"
    
    payload = {
        "name": "Fakhri",
        "job": "QA Automation Engineer"
    }
    
    response = requests.post(url, json=payload)
    
    assert response.status_code == 201
    
    response_data = response.json()
    assert response_data["name"] == "Fakhri"
    assert response_data["job"] == "QA Automation Engineer"
    
    assert "id" in response_data