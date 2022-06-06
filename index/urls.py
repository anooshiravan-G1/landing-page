from operator import index
from django.urls import path
from .views import indexView #, commentViews

urlpatterns= [
    path('', indexView.as_view(), name='indexPage'),
]