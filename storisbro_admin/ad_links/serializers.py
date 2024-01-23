from rest_framework import serializers
from .models import AdLinkModel


class AdLinkModelSerializer(serializers.ModelSerializer):
    link = serializers.CharField(read_only=True)
    
    class Meta:
        model = AdLinkModel
        fields = '__all__'