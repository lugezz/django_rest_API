import requests

endpoint = 'http://localhost:8000/api/products/'
data = {
    'title': 'Admin but not staff',
    'content': 'From post API with Model Mixin',
    'price': 9.99
}

# headers = {'Authorization': 'Token lalalal'}

# get_response = requests.post(endpoint, json=data, headers=headers)
get_response = requests.post(endpoint, json=data)

print(get_response.json())
print(get_response.status_code)
