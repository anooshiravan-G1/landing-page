from django.contrib import admin
from .models import ProjectForm
# Register your models here.

@admin.register(ProjectForm)
class index(admin.ModelAdmin):
    list_display = ['introduction', 'connection', 'challenge']
    list_filter = ['introduction', 'connection', 'challenge']
    search_fields = ['introduction', 'connection', 'challenge']
    list_display_links = ['introduction', 'connection', 'challenge']
