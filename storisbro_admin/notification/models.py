from django.db import models
from django.conf import settings
from django.utils import timezone

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    attachments = models.FileField(upload_to='attachments/', blank=True, null=True)
    scheduled_time = models.DateTimeField(default=timezone.now)
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return self.subject

# class StatusNotification(models.Model):
#     status = models.CharField(max_length=50, verbose_name="Статус уведомления")

class HistoryNotifications(models.Model):
    UID = models.CharField(max_length=150, verbose_name="UID пользователя", blank=True, null=True)
    title = models.CharField(max_length=250, verbose_name="Тема уведомления", null=True)
    text = models.TextField(verbose_name="Содержание уведомления")
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    file = models.FileField(verbose_name="Файл для уведомления", upload_to='files', blank=True, null=True)
    # start = models.DateTimeField(verbose_name="Дата отправки", blank=True)
    # status = models.ForeignKey(StatusNotification, on_delete=models.CASCADE)

    def __str__(self):
        return self.UID

