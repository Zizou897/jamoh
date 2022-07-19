from tabnanny import verbose
from django.db import models
from tinymce.models import HTMLField

# Create your models here.
from service.models import Convention

class Social(Convention):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    link = models.URLField(max_length=200)

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Sociaux'
    
    def __str__(self):
        return self.name

class Site(Convention):
    name = models.CharField(max_length=50)
    picture = models.FileField(upload_to='img_site')
    copy_right = HTMLField()
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'
    
    def __str__(self):
        return self.name

class Qualite(Convention):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length=50)
    text = models.CharField(max_length=250)
    description = HTMLField()
    
    class Meta:
        verbose_name = 'Qualite'
        verbose_name_plural = 'Qualites'
    
    def __str__(self):
        return self.name
    

class About(Convention):
    name = models.CharField(max_length=250)
    picture = models.FileField(upload_to='img_About')
    small_description = HTMLField()
    description = HTMLField()

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'
    
    def __str__(self):
        return self.name