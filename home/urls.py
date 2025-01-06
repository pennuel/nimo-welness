from django.contrib import admin
from django.urls import path, include

from home import views
from .views import newsletter_view, handle_newsletter_subscription

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('services/<str:service_name>/', views.service, name='service'),

    path('retreats/', views.retreats, name='retreats'),
    path('retreats/<str:retreat_name>/', views.retreat, name='retreat'),
    path ('rooms/', views.rooms, name='rooms'),
    path('newletter/', newsletter_view, name='news_letter'),
    path('subscribe/', handle_newsletter_subscription, name='subscribe')
]
