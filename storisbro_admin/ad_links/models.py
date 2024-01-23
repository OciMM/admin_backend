from django.db import models


class AdLinkModel(models.Model):
    link = models.CharField(max_length=150, unique=True, verbose_name="Рекламная ссылка")
    name = models.CharField(max_length=150, verbose_name="Название ссылки")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    clicks = models.PositiveIntegerField(default=0, verbose_name="Количество переходов")
    registration_client = models.PositiveIntegerField(
        default=0, 
        verbose_name="Количество зарегистрированных заказчиков"
    )
    registration_owner = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество зарегистрированных владельцев"
        )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Рекламная ссылка"
        verbose_name_plural = "Рекламные ссылки"