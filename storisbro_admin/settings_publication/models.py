from django.db import models
from django.core.validators import MaxValueValidator


class PublicationSettings(models.Model):
    publication_order = models.CharField(
        max_length=255,
        choices=[],
        default='content_ad_content',  # Значение по умолчанию
    )
    time_interval_between_publications = models.PositiveIntegerField(default=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._update_choices()

    def _update_choices(self):

        self._choices = [
            ('Content', 'Ad'),

        ]
        self._choices += [(x, x) for x in ['user_defined_1', 'user_defined_2']]  # Добавьте варианты, которые пользователь может определить сам

        # Обновляем поле choices
        self._meta.get_field('publication_order').choices = self._choices
class PublicationSettings(models.Model):
    CONTENT_VIDEO_CHOICES = [
        ('standard_mca', 'Standard MCA'),
        ('adult_sca', 'Adult SCA'),
    ]

    PUBLICATION_PERIOD_CHOICES = [
        ('constant', 'Constant Settings (X)'),
        ('custom', 'Custom Settings (Y)'),
    ]

    publication_date = models.DateField()
    content_video_type = models.CharField(max_length=20, choices=CONTENT_VIDEO_CHOICES)
    publication_period_type = models.CharField(max_length=20, choices=PUBLICATION_PERIOD_CHOICES)
    custom_settings_start_date = models.DateField(null=True, blank=True)
    custom_settings_end_date = models.DateField(null=True, blank=True)
    publication_time = models.TimeField()
    ad_slots_count = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(3)])
    content_video_priority = models.PositiveIntegerField(default=1)
    ad_story_priority = models.PositiveIntegerField(default=2)
    time_interval_between_publications = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.publication_date} - {self.content_video_type}'