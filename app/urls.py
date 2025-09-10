from django.urls import path
from .views import *

urlpatterns = [
    path("all-products/", all_products, name='all-products'),
    path("product/<id>/", single_product, name='single-product'),
]
