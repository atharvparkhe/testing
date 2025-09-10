from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product

@api_view(['GET'])
def all_products(request):
    try:
        return Response(ProductSerializer(Product.objects.all(), many=True).data)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def single_product(request, id):
    try:
        return Response(ProductSerializer(Product.objects.get(id=id)).data)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
