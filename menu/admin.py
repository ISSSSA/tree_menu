from django.contrib import admin
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'menu_name', 'url', 'parent')
    prepopulated_fields = {'url': ('title',)}


admin.site.register(MenuItem, MenuItemAdmin)
