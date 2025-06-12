from store.filters import ProductFilter
from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Count
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from .models import Product, Collection, OrderItem, Review
from .serializers import ProductSerializer, CollectionSerializer, ReviewSerializer
from rest_framework import status


# Create your views here.
class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(product_count=Count('products')).all().order_by('title')
    serializer_class = CollectionSerializer

    def destroy(self, request, *args, **kwargs):
        if Collection.objects.select_related('products').filter(id=kwargs['pk']).count() > 0:
            return Response({'error': 'Can not delete collection, contains one or more products'}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']

    def get_serializer_context(self):
        return {'request': self.request}
    
    def destroy(self, request, *args, **kwargs):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error: Can not delete product, associated to an order item.'}, status=status.HTTP_400_BAD_REQUEST)
        

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}