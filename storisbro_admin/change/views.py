from django.shortcuts import render, redirect
from .models import SiteSettings
from .forms import SiteSettingsForm
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from .models import  Statistics
import openpyxl
import datetime

def change_settings(request):
    site_settings = SiteSettings.objects.first()

    if request.method == 'POST':
        form = SiteSettingsForm(request.POST, instance=site_settings)
        if form.is_valid():
            form.save()
            messages.success(request, 'Настройки успешно изменены.')
            return redirect('change_settings')
    else:
        form = SiteSettingsForm(instance=site_settings)

    return render(request, 'change/change_settings.html', {'form': form})

#добавить аргументы пользователей, сообществ и т.д.


def generate_excel_file(request):
    # Получение начальной и конечной даты для фильтрации
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Конвертация строковых дат в объекты datetime
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()

    # Фильтрация данных по датам
    statistics = Statistics.objects.filter(date__range=(start_date, end_date)).first()

    # Создание книги и листа Excel
    wb = openpyxl.Workbook()
    ws = wb.active

    # Запись данных в лист Excel
    ws.append([])

    ws.append([])

    # Сохранение книги Excel
    excel_response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    excel_response['Content-Disposition'] = 'attachment; filename=statistics.xlsx'
    wb.save(excel_response)

    return excel_response