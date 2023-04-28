import requests

endpoint = 'http://127.0.0.1:8000/api/raw-home/'

get_response = requests.get(endpoint, params={'abc': 123}, json={'query': 'Hello World'})
# params is the same as making http://localhost:8000/api/?abc=123
print(get_response.json())
print(get_response.status_code)
