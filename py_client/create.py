import requests

endpoint = 'http://localhost:8000/api/products/'

get_response = requests.post(endpoint, json={
    'title': 'Hello DRF 2023 - Desde Terminal 2023',
    # 'content': 'From post API ya con Model Mixin',
    'price': 9.99
    })

print(get_response.json())
print(get_response.status_code)
