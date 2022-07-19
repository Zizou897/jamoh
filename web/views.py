from django.shortcuts import render, get_object_or_404


from service import models
from web import models as models_web
# Create your views here.

def index(request): 
    services = models.Service.objects.filter(status=True).order_by('order')[:6]
    sociaux = models_web.Social.objects.filter(status=True)
    sites = models_web.Site.objects.filter(status=True).first()
    qualites = models_web.Qualite.objects.filter(status=True)
    sousServices = models.SousService.objects.filter(status=True)[:9]
    abouts = models_web.About.objects.filter(status=True).first()
    servicesFooter = models.Service.objects.filter(status=True).order_by('-order')[:3]
    return render(request, "index.html", locals())


def detail_service(request, service_slug):
    serviceSlug = get_object_or_404(models.Service , service_slug=service_slug)
    donnees = models.Service.objects.filter(status=True)
    sites = models_web.Site.objects.filter(status=True).first()
   
    return render(request, "detail-service.html", locals())


def checkout(request, service_slug, sous_service_slug):
    sousServiceSlug = get_object_or_404(models.SousService, sous_service_slug=sous_service_slug)
    print(service_slug)
    return render(request,'chekout.html', locals())

def about(request):
    return render(request,'about.html', locals())


def inscription(request):
    return render(request,'inscription.html', locals())


def service(request):
    return render(request,'service.html', locals())
