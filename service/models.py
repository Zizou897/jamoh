from django.db import models
from django.utils.text import slugify


# Create your models here.


class Convention(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Service(Convention):
    picture = models.FileField(upload_to='img_service')
    name = models.CharField(max_length=50)
    order = models.IntegerField(default=0, null=True)
    text = models.TextField("")
    service_slug = models.SlugField()

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        if not self.service_slug:
            self.service_slug = slugify('{}'.format(self.name))
        return super().save(*args, **kwargs)

class SousService(Convention):
    picture = models.FileField(upload_to='img_SouService')
    name = models.CharField(max_length=50)
    price_mini = models.CharField(max_length=50)
    price_max = models.CharField(max_length=50)
    service = models.ForeignKey(Service, related_name='article_service',on_delete=models.CASCADE, blank=True)
    order = models.IntegerField(default=0)
    sous_service_slug = models.SlugField()

    class Meta:
        verbose_name = 'Sous Service'
        verbose_name_plural = 'Sous Services'
    
    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        if not self.sous_service_slug:
            self.sous_service_slug = slugify('{}'.format(self.name))
        return super().save(*args, **kwargs)
    
    