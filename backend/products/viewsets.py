from rest_framework import viewsets

from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    Get -> list -> Queryset
    Get -> retrieve -> Product instance detail view
    Post -> create -> New instance
    Put -> update
    Patch -> partial update
    Delete -> destroy
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # Default
