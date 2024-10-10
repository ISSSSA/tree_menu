from django import template
from ..models import MenuItem
from django.urls import resolve

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_url = resolve(context['request'].path_info).url_name
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')

    def build_menu_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent == parent:
                children = build_menu_tree(items, parent=item)
                tree.append({
                    'item': item,
                    'children': children,
                    'is_active': current_url == item.named_url
                })
        return tree

    menu_tree = build_menu_tree(menu_items)
    return {'menu_tree': menu_tree}