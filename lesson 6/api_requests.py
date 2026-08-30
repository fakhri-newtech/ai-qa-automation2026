import requests

print("--- Testing GET Request ---")
get_url = "https://reqres.in/api/users/2"
response = requests.get(get_url)

print(f"Status Code: {response.status_code}")
data = response.json()
print(f"User First Name: {data['data']['first_name']}")


print("\n--- Testing POST Request ---")
post_url = "https://reqres.in/api/users"

my_payload = {
    "name": "Fakhri",
    "job": "QA Automation Engineer"
}

post_response = requests.post(post_url, json=my_payload)

print(f"Status Code: {post_response.status_code}")
new_user_data = post_response.json()
print(f"Server replied with ID: {new_user_data['id']} for {new_user_data['name']}")