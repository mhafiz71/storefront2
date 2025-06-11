from django.urls import path
from . import views

#URLConfig
urlpatterns = [
    path('products/', views.products_list),
    path('products/<int:id>', views.product_detail),
    path('collections/<int:pk>', views.collection_detail, name='collection-detail')
]