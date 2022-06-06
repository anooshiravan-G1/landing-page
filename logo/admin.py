from django.contrib import admin
from .models import LogoForm
# Register your models here.

@admin.register(LogoForm)
class index(admin.ModelAdmin):
    list_display = ['cName', 'bName', 'email', 'wPhone', 'pPhone']
    list_filter = ['cName', 'bName', 'email', 'wPhone', 'pPhone']
    search_fields = ['cName', 'bName', 'email', 'wPhone', 'pPhone']
    list_display_links = ['cName', 'bName', 'email', 'wPhone', 'pPhone']
