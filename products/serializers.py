from rest_framework import serializers
from .models import Product
from products.util.generic import get_djust_price

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'description',
            'stock_quantity',
        ]
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['price'] = get_djust_price(representation['price'], representation['stock_quantity'])
        return representation