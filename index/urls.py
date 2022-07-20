from operator import index
from django.urls import path
from .views import indexView, services

urlpatterns= [
    path('', indexView.as_view(), name='indexPage'),
    path('service', services, name='service'),
]