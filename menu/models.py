from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True, null=True)  # URL может быть задан явно
    named_url = models.CharField(max_length=100, blank=True, null=True)  # Либо через named URL
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=50)  # Для идентификации меню по названию
    order = models.PositiveIntegerField(default=0)  # Для сортировки элементов меню

    def get_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
