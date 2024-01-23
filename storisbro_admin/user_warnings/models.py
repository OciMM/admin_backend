from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta
from django.utils import timezone

class GetFullUserModel(models.Model):
    get_user_id = models.IntegerField(verbose_name="Уникальный полученный ID", unique=True)
    name = models.CharField(max_length=150, verbose_name="Имя пользователя")
    email = models.EmailField(verbose_name="Электронная почта пользователя")
    account_vk = models.CharField(max_length=150, verbose_name="VK ID пользователя")
    set_user_id = models.CharField(max_length=50, unique=True, verbose_name="Созданный специальный UID")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Полученный пользователь"
        verbose_name_plural = "Полученные пользователи"


class WarningToUser(models.Model):
    """Модель сообщения об предупреждение"""
    user_id = models.ForeignKey(
        GetFullUserModel, 
        on_delete=models.CASCADE, 
        verbose_name="Пользователь"
        )
    
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


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Уникальное имя для связи с группами
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Уникальное имя для связи с разрешениями
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    username = models.CharField("Имя пользователя", max_length=200, unique=True)
    email = models.EmailField("Почта")
    password = models.CharField("Пароль", max_length=150)
    is_active = models.BooleanField(verbose_name="Статус", default=True)
    block_until = models.DateTimeField(null=True, blank=True)

    def block_for(self, duration):
        self.is_active = False
        self.block_until = timezone.now() + timedelta(days=duration)
        self.save()

    def check_block_status(self):
        if self.is_active and self.block_until and self.block_until < timezone.now():
            self.is_active = True  # Установить is_active в True, если время блокировки истекло
            self.block_until = None  # Сбросить время блокировки
            self.save()