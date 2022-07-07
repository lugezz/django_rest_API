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
