from django.db import models

from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     # Добавляем поля для определения, является ли пользователь владельцем или заказчиком
#     is_owner = models.BooleanField(default=False)
#     is_client = models.BooleanField(default=False)
