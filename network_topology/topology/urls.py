from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('get_devices/', views.get_devices, name='get_devices'),
    path('get_graph/', views.get_graph, name='get_graph'),
]
