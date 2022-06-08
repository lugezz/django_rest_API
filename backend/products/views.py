from rest_framework import authentication, generics, permissions

from .models import *
from .permissions import isStaffEditorPermission
from .serializers import *

from api.authentication import TokenAuthentication

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

        if not instance.content:
            instance.content = instance.title


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

""" No lo uso porque está el createList
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
 """    

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    #Permisos y autenticaciones
    authentication_classes = [
        authentication.SessionAuthentication,
        #authentication.TokenAuthentication #Original
        TokenAuthentication #Modificado por nosotros
        ]
    #permission_classes = [permissions.IsAuthenticated] Si está autenticado
    #puede hacer todo
    #permission_classes = [permissions.DjangoModelPermissions] #Aquí sigue los per-
    #misos definidos en Django Admin
    # La contra de Django permissions es que es limitado a cambios
    # Pero siempre va a dejar ver!
    permission_classes = [permissions.IsAdminUser, isStaffEditorPermission]
    
    def perform_create(self, serializer): #Frena antes de grabar
        #print (serializer.validated_data)

        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        
        serializer.save(content=content) #Listo, lo graba

