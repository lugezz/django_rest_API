from itertools import product
import json

from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import *
from products.serializers import *

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """ 
    DRF API VIEW
    """
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        #instance = serializer.save() <- Crea instancia

        print (serializer.data) # <- No crea una instancia

    return Response(serializer.data)