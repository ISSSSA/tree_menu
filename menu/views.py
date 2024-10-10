from django.shortcuts import render, get_object_or_404
from .models import MenuItem


def menu_item_view(request, menu_item_id=None):
    """
    Представление для обработки запросов к страницам пунктов меню.
    """
    if menu_item_id:
        menu_item = get_object_or_404(MenuItem, id=menu_item_id)
        context = {'menu_item': menu_item}
    else:
        context = {'menu_item': None}

    return render(request, 'menu_item.html', context)


def index(request):
    return render(request, 'index.html')
