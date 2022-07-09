from rest_framework import generics

from api.mixins import StaffEditorPermissionMixin, UserQuerysetMixin
from products.models import Product
from products.serializers import ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(UserQuerysetMixin,
                           StaffEditorPermissionMixin,
                           generics.UpdateAPIView
                           ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

        if not instance.content:
            instance.content = instance.title


class ProductDeleteAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductListCreateAPIView(UserQuerysetMixin,
                               StaffEditorPermissionMixin,
                               generics.ListCreateAPIView
                               ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Permisos y autenticaciones
    # Definido en settings ahora
    # authentication_classes = [
    #    authentication.SessionAuthentication,
    #    authentication.TokenAuthentication #Original
    #    TokenAuthentication  # Modificado por nosotros
    #    ]
    # permission_classes = [permissions.IsAuthenticated] Si está autenticado
    # puede hacer todo
    # permission_classes = [permissions.DjangoModelPermissions] #Aquí sigue los per-
    # misos definidos en Django Admin
    # La contra de Django permissions es que es limitado a cambios
    # Pero siempre va a dejar ver!

    def perform_create(self, serializer):  # Frena antes de grabar
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title

        serializer.save(user=self.request.user, content=content)  # Listo, lo graba
