from django.urls import path
from .views import change_publication_order

urlpatterns = [
    path('change_order/<int:settings_id>/', change_publication_order, name='change_publication_order'),

]