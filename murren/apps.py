from django.apps import AppConfig


class MurrenConfig(AppConfig):
    name = 'murren'

    def ready(self):
        import murren.signals
