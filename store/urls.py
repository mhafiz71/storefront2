from django.urls import path
from rest_framework_nested import routers
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

#URLConfig
router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='product')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('orders', views.OrderViewset)
router.register('customers', views.CustomerViewset, basename='customer')

product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', views.CartItemViewSet, basename='cart-items')
urlpatterns = router.urls + product_router.urls + cart_router.urls