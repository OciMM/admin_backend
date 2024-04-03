from django.db import models
# from django.contrib.auth.models import AbstractUser
from datetime import timedelta
from django.utils import timezone


class WarningToUser(models.Model):
    """Модель сообщения об предупреждение"""
    message_service = models.BooleanField(verbose_name="Личный кабинет на сервисе", default=False)
    message_vk = models.BooleanField(verbose_name="Сообщение Вконтакте", default=False)
    message_email = models.BooleanField(verbose_name="Электронная почта", default=False)
    text = models.TextField(verbose_name="Текст предупреждения")
    date = models.DateField(verbose_name="Дата предупреждения", auto_now_add=True)

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = "Отправка предупреждения"
        verbose_name_plural = "Отправка предупреждений"


# class CustomUser(AbstractUser):
#     pass