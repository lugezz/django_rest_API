import requests

endpoint = 'http://localhost:8000/api/'

# get_response = requests.post(endpoint, json={
#     'title': 'Hello World Chulo',
#     'content': 'From post',
#     'price': 8.88
#     })

get_response = requests.post(endpoint, json={'product_id': 2})

print(get_response.json())
print(get_response.status_code)
