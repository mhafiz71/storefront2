from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection, Review

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'product_count']
    product_count = serializers.IntegerField(read_only=True)

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

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description', 'date']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)
    