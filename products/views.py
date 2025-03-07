import traceback
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from.models import Product
from.serializers import ProductSerializer


class ListCreateProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class GetUpdateProductDetails(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]