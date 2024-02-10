from django.urls import path
from .views import registered_users_count, generate_excel_file

urlpatterns = [
    path('registered_users/', registered_users_count, name='registered_users_count'),
    path('generate_excel/', generate_excel_file, name='generate_excel_file'),
]