import json

from django.http import JsonResponse


def api_home(request):
    # request -> HttpRequest -> Django

    print(request.GET)  # Devuelve los parámetros

    # request.body
    body = request.body  # Perecería JSON Data, pero es Byte String of JSON data
    print(body)  # b'{"query": "Hello World"}'
    # Para transformarlo a JSON
    data = {}
    try:
        data = json.loads(body)
    except Exception:
        pass

    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    # return JsonResponse({'message': 'Hi there, this is your Django API response'})
    return JsonResponse(data)
