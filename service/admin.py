from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models
# Register your models here.


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('image_view', 'name', 'order', 'status')
    list_display_links = ('image_view', 'name',)
    list_editable = ['status']

    def image_view(self, obj):
        return mark_safe(f'<img src= "{obj.picture.url}" style ="height:100px; width:200px>"')
    image_view.short_description = "aperçu des images"


@admin.register(models.SousService)
class SousServiceAdmin(admin.ModelAdmin):
    list_display = ('image_view', 'name', 'service','price_mini', 'status')
    list_display_links = ('image_view', 'name',)
    list_editable = ['status']

    def image_view(self, obj):
        return mark_safe(f'<img src= "{obj.picture.url}" style ="height:100px; width:200px>"')
    image_view.short_description = "aperçu des images"
