from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('inscription/', views.inscription, name="inscription"),
    path('service/', views.service, name="service"),
    path('<str:service_slug>/', views.detail_service, name="detail-service"),
    path('<str:service_slug>/<str:sous_service_slug>/confirm/', views.checkout, name="checkout"),
]
