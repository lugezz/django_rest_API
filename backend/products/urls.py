from django.urls import path

from .views import (
    ProductDeleteAPIView, ProductDetailAPIView,
    ProductListCreateAPIView, ProductUpdateAPIView
)


urlpatterns = [
    # path('', ProductListAPIView.as_view()),
    path('', ProductListCreateAPIView.as_view(), name='product-list'),
    path('<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='product-delete'),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
]
