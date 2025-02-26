from django.apps import AppConfig


class HapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Hapi'

    def ready(self):
        import Hapi.signals 
