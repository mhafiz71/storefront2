from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'description', 'inventory' ,'unit_price', 'price_with_tax', 'collection']
    price_with_tax = serializers.SerializerMethodField(method_name="calc_tax")


    def calc_tax(self, prodcut: Product):
        return prodcut.unit_price * Decimal(1.1)  

    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.new_field = 32
    #     product.save()
    #     return product
    
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title')
    #     instance.save()
    #     return instance
