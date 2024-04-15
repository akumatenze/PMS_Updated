from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CORE'

# apps.py

from django.apps import AppConfig

class OCIConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'OCI'

    def ready(self):
        import OCI.signals # type: ignore
