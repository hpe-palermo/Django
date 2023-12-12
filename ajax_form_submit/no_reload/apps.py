from django.apps import AppConfig


class NoReloadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'no_reload'
