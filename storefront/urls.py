"""storefront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.permissions import AllowAny
from store.views import CookieTokenObtainPairView, CookieTokenRefreshView, logout_view

class SpectacularAPIViewNoAuth(SpectacularAPIView):
    permission_classes = [AllowAny]

class SpectacularSwaggerViewNoAuth(SpectacularSwaggerView):
    permission_classes = [AllowAny]

class SpectacularRedocViewNoAuth(SpectacularRedocView):
    permission_classes = [AllowAny]

admin.site.site_title = 'Storefront Admin Login'
admin.site.site_header = 'Storefront Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),
    path('store/', include('store.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('auth/', include('djoser.urls')),
    path('api/token/', CookieTokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', CookieTokenRefreshView.as_view(), name='refresh'),
    path('api/token/logout/', logout_view, name='logout'),

    path('api/schema/', SpectacularAPIViewNoAuth.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerViewNoAuth.as_view(), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocViewNoAuth.as_view(), name='redoc'),
]
