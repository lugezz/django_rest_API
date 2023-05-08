from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import api_home, mdt_product, raw_home, raw_product


urlpatterns = [
    path('', api_home),

    path('products/', include('products.urls')),
    path('articles/', include('articles.urls')),
    path('search/', include('search.urls')),

    path('auth/', obtain_auth_token),

    # JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('raw-home/', raw_home, name='raw_home'),
    path('raw-product/', raw_product, name='raw_product'),
    path('mdt-product/', mdt_product, name='mdt_product'),
]
