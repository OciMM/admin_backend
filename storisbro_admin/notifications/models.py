from django.db import models


class AutoNotificationModel(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название уведомление")
    text_positive = models.TextField(verbose_name='"Позитивный" текст уведомления')
    text_negative = models.TextField(verbose_name='"Отрицательный" текст уведомления')
    message_service = models.BooleanField(verbose_name="Личный кабинет на сервисе", default=False)
    message_vk = models.BooleanField(verbose_name="Сообщение Вконтакте", default=False)
    message_email = models.BooleanField(verbose_name="Электронная почта", default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Автоматическое уведомление"
        verbose_name_plural = "Автоматические уведомления"