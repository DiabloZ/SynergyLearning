from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'News'
    verbose_name = "Новости"


class HimanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Human'
    verbose_name = "Люди"