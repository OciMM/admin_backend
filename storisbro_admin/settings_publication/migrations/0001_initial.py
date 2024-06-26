# Generated by Django 4.2.9 on 2024-02-10 08:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_date', models.DateField()),
                ('content_video_type', models.CharField(choices=[('standard_mca', 'Standard MCA'), ('adult_sca', 'Adult SCA')], max_length=20)),
                ('publication_period_type', models.CharField(choices=[('constant', 'Constant Settings (X)'), ('custom', 'Custom Settings (Y)')], max_length=20)),
                ('custom_settings_start_date', models.DateField(blank=True, null=True)),
                ('custom_settings_end_date', models.DateField(blank=True, null=True)),
                ('publication_time', models.TimeField()),
                ('ad_slots_count', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(3)])),
                ('content_video_priority', models.PositiveIntegerField(default=1)),
                ('ad_story_priority', models.PositiveIntegerField(default=2)),
                ('time_interval_between_publications', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
