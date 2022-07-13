from dataclasses import Field
from itertools import product
from rest_framework import serializers
from mercado.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'quantidade']
