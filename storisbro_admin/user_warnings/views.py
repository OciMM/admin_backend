from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import WarningToUser
from .serializers import WarningToUserSerializer
from .services import create_user_id, send_message_vk, send_message_email
import requests


# class GetUserListAPIView(ListAPIView):
#     queryset = GetFullUserModel.objects.all()
#     serializer_class = GetUserListSerializer


# class GetUserAPIView(APIView):
#     """Получение информации о пользователе"""
#     def get(self, request, pk, *args, **kwargs):
#         # URL для получения данных из API проекта №1
#         url_project1_api = f'http://127.0.0.1:8000/user/{pk}'

#         # Отправка GET запроса к API проекта №1
#         response = requests.get(url_project1_api)

#         if response.status_code == 200:
#             # Если запрос успешен, возвращаем полученные данные
#             data = response.json()
#             user_instance, created = GetFullUserModel.objects.update_or_create(
#                 defaults={
#                     'get_user_id': data.get('id'),
#                     'name': data.get('name'),
#                     'email': data.get('email'),
#                     'account_vk': data.get('account_vk'),
#                     'set_user_id': create_user_id()
#                 } 
#             )
#             return Response(data)
#         else:
#             # Если возникла ошибка, возвращаем соответствующий ответ
#             return Response({'error': 'Failed to fetch data from Project 1'}, status=status.HTTP_400_BAD_REQUEST)
        

# class WarningToUserAPIView(APIView):
#     def get(self, request):
#         warning_model = WarningToUser.objects.all()
#         serializer = WarningToUserSerializer(warning_model, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = WarningToUserSerializer(data=data)
        
#         if serializer.is_valid():
#             # Сохраняем данные
#             warning_instance = serializer.save()

#             # Получаем пользователя по предоставленному ID
#             user_id = data.get('user_id')  # Предполагается, что user_id передается в запросе
#             user = GetFullUserModel.objects.get(id=user_id)

#             # Проверяем, равно ли поле message_vk True
#             if warning_instance.message_vk:
#                 # Отправляем сообщение в VK
#                 message_text = data.get('text')
#                 account_vk = user.account_vk
#                 send_message_vk(account_vk, message_text)

#             if warning_instance.message_email:
#                 # Отправляем сообщение по электронной почте
#                 message_text = data.get('text')
#                 message_email = user.email
#                 send_message_email(message_email, message_text)  # Здесь вызываем вашу функцию отправки почты

#             return Response({"message": "Данные успешно обработаны"}, status=status.HTTP_200_OK)
            
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# class CustomUserAPIView(APIView):
#     def get(self, request):
#         user_model = CustomUser.objects.all()
#         serializer = CustomUserSerializer(user_model, many=True)
#         return Response(serializer.data)
    

# class PK_CustomUserAPIView(APIView):
#     def get(self, request, pk):
#         user_model = CustomUser.objects.get(pk=pk)
#         serializer = CustomUserSerializer(user_model)
#         return Response(serializer.data)
    
#     def patch(self, request, pk):
#         instance = CustomUser.objects.get(pk=pk)
        
#         serializer = CustomUserSerializer(instance, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
                
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
