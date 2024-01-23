from rest_framework import serializers
from .models import WarningToUser, GetFullUserModel, CustomUser


class GetUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetFullUserModel
        fields = '__all__'

class WarningToUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarningToUser
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
