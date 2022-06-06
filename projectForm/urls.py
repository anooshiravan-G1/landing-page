from django.urls import path
from .views import projectView, projectConfirm

urlpatterns= [
    path('projects', projectView.as_view(), name='projectPage'),
     path('projectConfirm',projectConfirm,name="projectConfirm"),
]