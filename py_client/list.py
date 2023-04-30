import requests
from getpass import getpass

endpoint = 'http://localhost:8000/api/auth/'
username = input("What's your username?\n")
password = getpass("What's your password?\n")

auth_response = requests.post(
    endpoint,
    json={'username': username, 'password': password}
    )
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    # Si lo borro de admin, crea uno distinto
    headers = {
        'Authorization': f'Token {token}'
    }

    endpoint = 'http://localhost:8000/api/products/'

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
    print(get_response.status_code)
