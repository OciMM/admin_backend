from rest_framework import serializers
from .models import AutoNotificationModel


class AutoNotificationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoNotificationModel
        fields = '__all__'