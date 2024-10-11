from django.shortcuts import render, get_object_or_404
from .models import MenuItem


def menu_item_view(request, menu_item_id=None):
    menu_item = get_object_or_404(MenuItem, id=menu_item_id)
    return render(request, 'menu_item.html', {'menu_item': menu_item})
