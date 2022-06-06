from django.contrib import admin
from .models import Index

# Register your models here.
@admin.register(Index)
class index(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'workName', 'email']
    list_filter = ['name', 'phone_number', 'workName', 'email']
    search_fields = ['name', 'phone_number', 'workName', 'email']
    list_display_links = ['name', 'phone_number', 'email']
    

        
