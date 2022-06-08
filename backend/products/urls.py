from django.urls import path

from .views import *

urlpatterns = [
    # path('', ProductListAPIView.as_view()),
    path('', ProductListCreateAPIView.as_view()),
    path('<int:pk>/update', ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete', ProductDeleteAPIView.as_view()),
    path('<int:pk>/', ProductDetailAPIView.as_view()),
]