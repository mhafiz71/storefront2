from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from .models import LikedItem

# Register your models here.
@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    search_fields = ['content_type']


@admin.register(LikedItem)
class LikedItemdAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user', 'content_type']
    search_fields = ['user']
    list_display = ['user', 'content_type']