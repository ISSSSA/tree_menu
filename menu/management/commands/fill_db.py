from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = 'Fill the database with predefined menu items'

    def handle(self, *args, **kwargs):
        sql_script = """
        INSERT INTO menu_menuitem (title, parent_id, menu_name, url, named_url,"order") VALUES
('Главная', NULL, 'main_menu', '/main_menu/home/', NULL,1),
('О нас', NULL, 'main_menu', '/main_menu/about/', NULL,1),
('Услуги', NULL, 'main_menu', '/main_menu/services/', NULL,1),
('Контакты', NULL, 'main_menu', '/main_menu/contact/', NULL,1),
('Блог', NULL, 'main_menu', '/main_menu/blog/', NULL,1);

-- Вставляем вложенные пункты меню
INSERT INTO menu_menuitem (title, parent_id, menu_name, url, named_url,"order") VALUES
('Наша команда', 2, 'main_menu', '/main_menu/about/our-team/', NULL,1),
('Наша миссия', 2, 'main_menu', '/main_menu/about/our-mission/', NULL,2),
('Дизайн', 3, 'main_menu', '/main_menu/services/design/', NULL,1),
('Разработка', 3, 'main_menu', '/main_menu/services/development/', NULL,2),
('SEO', 3, 'main_menu', '/main_menu/services/seo/', NULL,3),
('Статьи', 5, 'main_menu', '/main_menu/blog/articles/', NULL,1),
('Новости', 5, 'main_menu', '/main_menu/blog/news/', NULL,2); """

        with connection.cursor() as cursor:
            cursor.executescript(sql_script)

        self.stdout.write(self.style.SUCCESS('Database has been filled with menu items.'))
