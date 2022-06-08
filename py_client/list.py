import requests
from getpass import getpass

endpoint = 'http://localhost:8000/api/auth/'
password = getpass()

auth_response = requests.post(endpoint, 
    json={'username': 'staff', 'password': password}
    )
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    #Si lo borro de admin, crea uno distinto
    headers = {
        'Authorization': f'Bearer {token}'
    }

    endpoint = 'http://localhost:8000/api/products/'

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
    print(get_response.status_code)

