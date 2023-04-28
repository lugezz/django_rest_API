import json

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer

# from products.models import Product


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):  # Retorning very detailed info of error
        print(serializer.data)
        data = serializer.data

        return Response(data)


def raw_home(request, *args, **kwargs):
    # print(dir(request))
    # print(request.__dict__)
    body = request.body
    data = {}

    try:
        data = json.loads(body)  # json.loads converts json to python dict
    except Exception:
        pass

    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    data['params'] = dict(request.GET)

    print(data)
    # return JsonResponse({"message": "Hello World, this is your API response"})

    return JsonResponse(data)
