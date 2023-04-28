import requests


endpoint = 'http://httpbin.org/status/200'
# endpoint = 'http://httpbin.org/'

get_response = requests.get(endpoint)  # Es una HTTP Request
# API -> Method Application Program Interface
print(get_response.text)
print(get_response.status_code)

# HTTP Request -> HTML, for example for 'http://httpbin.org/'
# REST API HTTP Request -> JSON for status 200

endpoint = 'http://httpbin.org/anything'
get_response = requests.get(endpoint, json={'query': 'Hello World'})
# json argument can add information
print(get_response.json())
print(get_response.status_code)
