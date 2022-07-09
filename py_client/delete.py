import requests

id = input('Ingrese el id de producto que quiere usar: ')

try:
    mId = int(id)

except Exception:
    mId = None
    print(f'{id} no es un id válido')

if mId:
    endpoint = f'http://localhost:8000/api/products/{mId}/delete'
    get_response = requests.delete(endpoint)

    print(get_response.status_code, get_response.status_code == 204)
