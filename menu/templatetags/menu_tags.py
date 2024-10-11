from django import template
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path_info
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')

    def build_menu_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent == parent:
                children = build_menu_tree(items, parent=item)
                is_active = current_url.startswith(item.get_url())
                print(parent)
                tree.append({
                    'item': item,
                    'children': children,
                    'is_active': is_active or any(child['is_active'] for child in children),
                    'parent': parent
                })
        return tree

    menu_tree = build_menu_tree(menu_items)
    return {'menu_tree': menu_tree, 'current_url': current_url}
