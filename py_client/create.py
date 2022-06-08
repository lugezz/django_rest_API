import requests

endpoint = 'http://localhost:8000/api/products/'

get_response = requests.post(endpoint, json={
    'title': 'Hello World ChuloAPI - Mixin',
    #'content': 'From post API ya con Model Mixin',
    'price': 7.77
    })

print(get_response.json())
print(get_response.status_code)