from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import AutoNotificationModel
from .serailizers import AutoNotificationModelSerializer


class AutoNotificationModelAPIView(APIView):
    def get(self, request):
        notification_model = AutoNotificationModel.objects.all()
        serializer = AutoNotificationModelSerializer(notification_model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = AutoNotificationModelSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

class PK_AutoNotificationModelAPIView(APIView):
    def get(self, request, pk):
        notification_model = AutoNotificationModel.objects.get(pk=pk)
        serializer = AutoNotificationModelSerializer(notification_model)
        return Response(serializer.data)
    
    def patch(self, request, pk):
        instance = AutoNotificationModel.objects.get(pk=pk)
        
        serializer = AutoNotificationModelSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
