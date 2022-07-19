from django.contrib import admin
from django.utils.safestring import mark_safe
from web import models
# Register your models here.



@admin.register(models.Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'link', 'status')
    list_editable = ('status',)

@admin.register(models.Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('image_view', 'name', 'email', 'status')
    list_display_links = ('image_view', 'name')
    list_editable = ('status',)

    def image_view(self, obj):
        return mark_safe(f'<img src= "{obj.picture.url}" style ="height:100px; width:200px>"')
    image_view.short_description = "aperçu des images"


@admin.register(models.Qualite)
class QualiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'date_add', 'status')
    list_editable = ('status',)


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('image_view', 'name', 'small_description', 'status')
    list_display_links = ('image_view', 'name')
    list_editable = ('status',)
    
    def image_view(self, obj):
        return mark_safe(f'<img src= "{obj.picture.url}" style ="height:100px; width:200px>"')
    image_view.short_description = "aperçu des images"