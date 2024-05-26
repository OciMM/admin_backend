from rest_framework import serializers
from .models import HistoryNotifications


class HistoryNotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryNotifications
        fields = '__all__'