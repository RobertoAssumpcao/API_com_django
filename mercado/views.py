# from django.shortcuts import render
from rest_framework import viewsets
from mercado.models import Product
from mercado.serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




