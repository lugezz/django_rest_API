import requests

#endpoint = 'http://httpbin.org/status/200/'
endpoint = 'http://httpbin.org/'

get_response = requests.get(endpoint) #Es una HTTP Request
#API -> Method Application Program Interface
print(get_response.text)

#HTTP Request -> HTML el ejemplo de recient
#REST API HTTP Request -> JSON el ejemplo próximo

endpoint = 'http://httpbin.org/anything'
get_response = requests.get(endpoint, json={'query': 'Hello World'}) 
# El argumento json es si quiero agregarle información
print(get_response.json())

