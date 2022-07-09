import requests

endpoint = 'http://localhost:8000/api/products/2/update/'

data = {  # Es lo que quiero cambiar
    'title': 'Hello world my old friend cordobes',
    'content': 'Update desde terminal',
    'price': 119.99
}
get_response = requests.put(endpoint, json=data)

print(get_response.json())
print(get_response.status_code)
