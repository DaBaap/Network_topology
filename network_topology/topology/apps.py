from django.apps import AppConfig


class TopologyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'topology'

    def ready(self):
        # Import and execute the graph-building function
        from .graph import build_graph
        build_graph()
