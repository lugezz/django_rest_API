from django.forms import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(['GET'])
def api_home(request):
    """
    DRF API VIEW
    """
    instance = Product.objects.first()

    data = {}

    if instance:
        # data = ProductSerializer(instance).data
        data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])

    return Response(data)
