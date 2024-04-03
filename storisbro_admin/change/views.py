from django.shortcuts import render, redirect
from .models import SiteSettings
from .forms import SiteSettingsForm
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
import openpyxl
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChangeSettingsSerializer


class ChangeSettingsAPIView(APIView):
    def get(self, request):
        setting_model = SiteSettings.objects.all()
        serializer = ChangeSettingsSerializer(setting_model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ChangeSettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangeSettingsAPIViewPK(APIView):
    def get(self, request, pk):
        setting_model = SiteSettings.objects.get(pk=pk)
        serializer = ChangeSettingsSerializer(setting_model)
        return Response(serializer.data)
    
    def patch(self, request, pk):
        instance = SiteSettings.objects.get(pk=pk)
        serializer = ChangeSettingsSerializer(instance, data=request.data, partial=True)  # partial=True для частичного обновления
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#добавить аргументы пользователей, сообществ и т.д.


# def generate_excel_file(request):
#     # Получение начальной и конечной даты для фильтрации
#     start_date_str = request.GET.get('start_date')
#     end_date_str = request.GET.get('end_date')

#     # Проверка наличия дат в запросе
#     if not (start_date_str and end_date_str):
#         # Возвращайте ошибку или обработайте ситуацию, когда даты не указаны
#         return HttpResponse("Не указаны начальная и/или конечная дата")

#     # Конвертация строковых дат в объекты datetime
#     start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
#     end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d").date()

#     # Фильтрация данных по датам
#     statistics = Statistics.objects.filter(date__range=(start_date, end_date)).all()

#     # Создание книги и листа Excel
#     wb = openpyxl.Workbook()
#     ws = wb.active

#     # Запись заголовка в лист Excel
#     ws.append(["Дата", "Значение"])  # Замените заголовки на актуальные поля из вашей модели

#     # Запись данных в лист Excel
#     for stat in statistics:
#         ws.append([stat.date, stat.value])  # Подставьте актуальные поля из вашей модели

#     # Сохранение книги Excel
#     excel_response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#     excel_response['Content-Disposition'] = 'attachment; filename=statistics.xlsx'
#     wb.save(excel_response)

#     return excel_response