from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    
    if method == 'GET':
        #GET Request -> DetailView / ListView
        if pk is not None:
            #DetailView
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj).data

            return Response(data)
        
        #ListView
        queryset = Product.objects.all()
        data = ProductSerializer(queryset).data
        return Response(data)
    else:
        #POST Request -> Create
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
        
            serializer.save(content=content) #Listo, lo graba

            return Response(serializer.data)


