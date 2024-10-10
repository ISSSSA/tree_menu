# Register your models here.
from django.contrib import admin
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'menu_name', 'parent', 'order']
    list_filter = ['menu_name']
    ordering = ['menu_name', 'parent', 'order']


admin.site.register(MenuItem, MenuItemAdmin)
