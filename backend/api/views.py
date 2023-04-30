import json

from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer

from products.models import Product


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):  # Retorning very detailed info of error
        data = serializer.data
        print(data)

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


def raw_product(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}

    if model_data is None:
        return JsonResponse({"message": "No data found"})
    else:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price

    return JsonResponse(data)


def mdt_product(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()

    if model_data is None:
        return JsonResponse({"message": "No data found"})
    else:
        data = model_to_dict(model_data)
        return JsonResponse(data)
