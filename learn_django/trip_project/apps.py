from django.apps import AppConfig


class TripProjectConfig(AppConfig):
    name = 'trip_project'

    def ready(self):
        from .signals import create_profile
