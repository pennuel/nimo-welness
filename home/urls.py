from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('service/<str:services_selected>/', views.service_details, name='service'),
    path('services/', views.service, name='service')
]
