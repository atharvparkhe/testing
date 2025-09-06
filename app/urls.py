from django.urls import path
from .views import *

urlpatterns = [
    path("products/", MyListCreateAPIView.as_view(), name='product-list'),
    path("products/<int:id>/", MyRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
]
