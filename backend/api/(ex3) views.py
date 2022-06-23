from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(['POST'])
def api_home(request):
    """
    DRF API VIEW
    """
    instance = Product.objects.first()
    print(instance.title, instance.content)

    data = request.data

    if instance:
        data = ProductSerializer(instance).data

    return Response(data)
