from django.contrib import admin
from django.urls import path

from menu.services.url_service import DynamicMenuURl

urlpatterns = [
    path('admin/', admin.site.urls), *DynamicMenuURl(None).dynamic_urls
]
