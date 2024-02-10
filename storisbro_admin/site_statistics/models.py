from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Добавляем поля для определения, является ли пользователь владельцем или заказчиком
    is_owner = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)

class Statistics(models.Model):
    registered_users = models.IntegerField(default=0)
    unique_visits = models.IntegerField(default=0)
    refills = models.IntegerField(default=0)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    admin_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    creative_uploads = models.IntegerField(default=0)
    community_uploads = models.IntegerField(default=0)
    story_views = models.IntegerField(default=0)