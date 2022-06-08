from itertools import product
import json

from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import *
from products.serializers import *

@api_view(['POST'])
def api_home(request):
    """ 
    DRF API VIEW
    """
    instance = Product.objects.first()
    print (instance.title, instance.content)

    data = request.data

    if instance:
        data = ProductSerializer(instance).data

    return Response(data)