from django.urls import path
from ..models import MenuItem
from ..views import menu_item_view


class DynamicMenuURl:

    def __init__(self, get_response):
        self.get_response = get_response
        self.dynamic_urls = self._load_urls_from_db()

    @staticmethod
    def _load_urls_from_db():
        menu_items = MenuItem.objects.all()
        dynamic_urls = []
        for item in menu_items:
            dynamic_urls.append(path(item.get_url()[1:], menu_item_view, {'menu_item_id': item.id}, name=item.title))
        return dynamic_urls
