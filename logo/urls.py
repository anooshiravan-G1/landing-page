from django.urls import path
from .views import logoView, logoConfirm

urlpatterns= [
    path('logo', logoView.as_view(), name='logoPage'),
    path('logoConfirm', logoConfirm, name='logoConfirm'),
]