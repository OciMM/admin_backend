from rest_framework import serializers
from .models import WarningToUser


class WarningToUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarningToUser
        fields = '__all__'
