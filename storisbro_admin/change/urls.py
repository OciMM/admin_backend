from django.urls import path
from .views import change_settings

urlpatterns = [
    path('change_settings/', change_settings, name='change_settings'),
]