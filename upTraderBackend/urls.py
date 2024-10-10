from django.contrib import admin
from django.urls import path

from menu.models import MenuItem
from menu.views import index, menu_item_view


def generate_menu_urls():
    """
    Функция для создания URL-маршрутов для всех элементов меню.
    """
    urlpatterns = []
    menu_items = MenuItem.objects.all()

    for item in menu_items:
        if item.url:  # Если явно задан URL
            urlpatterns.append(
                path(item.url.lstrip('/'), menu_item_view, {'menu_item_id': item.id}, name=item.title)
            )
        elif item.named_url:  # Если задан named URL
            urlpatterns.append(
                path(item.get_url().lstrip('/'), menu_item_view, {'menu_item_id': item.id}, name=item.named_url)
            )

    return urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu_item_view, {'menu_item_id': None}, name='index'),  #
]

urlpatterns += generate_menu_urls()
