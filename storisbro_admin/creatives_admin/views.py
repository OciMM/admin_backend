from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
import requests

class CheckAllAdminCreativesListAPIView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        # URL для получения данных из API проекта №1
        url_project1_api = 'http://127.0.0.1:8000/api_creatives/all_creatives'

        # Отправка GET запроса к API проекта №1
        response = requests.get(url_project1_api)

        if response.status_code == 200:
            # Если запрос успешен, возвращаем полученные данные
            data = response.json()
            return Response(data)
        else:
            # Если возникла ошибка, возвращаем соответствующий ответ
            return Response({'error': 'Failed to fetch data from Storisbro'}, status=status.HTTP_400_BAD_REQUEST)


class CheckCreativesAPIView(APIView):
    def get(self, request, pk, type_creative, *args, **kwargs):
        # URL для получения данных из API проекта №1
        url_project1_api = f'http://127.0.0.1:8000/api_creatives/{type_creative}/{pk}'

        # Отправка GET запроса к API проекта №1
        response = requests.get(url_project1_api)

        if response.status_code == 200:
            # Если запрос успешен, возвращаем полученные данные
            data = response.json()
            return Response(data)
        else:
            # Если возникла ошибка, возвращаем соответствующий ответ
            return Response({'error': 'Failed to fetch data from Project 1'}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk):
        # Получаем данные для обновления из запроса
        data_to_update = request.data

        # URL для отправки PATCH запроса к API проекта №1 с использованием pk из URL
        url_project1_api = f'http://127.0.0.1:8000/api_creatives/add_single_creative/{pk}'  # Пример URL для обновления объекта с определенным id

        # Отправка PATCH запроса к API проекта №1
        response = requests.patch(url_project1_api, data=data_to_update)

        if response.status_code == 200:
            # Если запрос успешен, возвращаем сообщение об успешном обновлении
            return Response({'message': f'Data updated successfully for object with id={pk} in Project 1'})
        else:
            # Если возникла ошибка, возвращаем соответствующий ответ
            return Response({'error': f'Failed to update data for object with id={pk} in Project 1'}, status=status.HTTP_400_BAD_REQUEST)  