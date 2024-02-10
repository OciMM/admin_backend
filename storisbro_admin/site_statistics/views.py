from django.db.models import Sum
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from .models import Statistics, Transaction, Creative, Community, Story
import logging
import openpyxl
from django.http import HttpResponse
import os
from datetime import datetime, timedelta
import pytz
from django.conf import settings
BASE_DIR = settings.BASE_DIR

# Получение количества ошибок из лог-файла
def get_error_count_from_logs():
    log_file_path = os.path.join(BASE_DIR, 'logs', 'errors.log')

    try:
        with open(log_file_path, 'r') as file:
            # Подсчет строк, представляющих собой записи об ошибках
            error_lines = [line for line in file if 'ERROR' in line]

            # Получение общего количества ошибок
            error_count = len(error_lines)
            return error_count
    except FileNotFoundError:
        # В случае отсутствия файла логов
        return 0

# Использование функции для получения количества ошибок
total_error_count = get_error_count_from_logs()

def registered_users_count(request):
    # Получение количества зарегистрированных пользователей
    user_count = User.objects.count()

    owners = User.objects.filter(is_owner=True).count()
    clients = User.objects.filter(is_client=True).count()

    # Получение количества уникальных и общих посещений
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    total_visits = len(sessions)

    # Обновление статистики
    statistics = Statistics.objects.first()
    statistics.registered_users = user_count

    # Вычисление предыдущего дня
    previous_day = timezone.now() - timedelta(days=1)
    previous_day = previous_day.replace(hour=0, minute=0, second=0, microsecond=0)

    # Фильтрация транзакций по предыдущему дню
    refill_transactions = Transaction.objects.filter(type='refill', date__gte=previous_day)
    withdrawal_transactions = Transaction.objects.filter(type='withdrawal', date__gte=previous_day)

    # Расчет заработка админов 
    # admins_earnings = a #добавить доход админов
    #  модель Creative для отслеживания загруженных креативов
    creative_count = Creative.objects.filter(date__gte=previous_day).count()
    statistics.creative_uploads = creative_count

    #  модель Community для отслеживания загруженных сообществ
    community_count = Community.objects.filter(date__gte=previous_day).count()
    statistics.community_uploads = community_count

    #  модель Community для отслеживания загруженных сообществ
    story_views_count = Story.objects.filter(date__gte=previous_day).aggregate(Sum('views')).get('views__sum', 0)
    statistics.story_views = story_views_count

    statistics.save()

    # Передача значений в шаблон
    return render(request, 'registered_users_count.html', {
        'user_count': user_count, #количество юзеров
        'total_visits': total_visits, #количество посетителей
        'refill_transactions': refill_transactions, #депозит
        'withdrawal_transactions': withdrawal_transactions, #вывод
        # 'admins_earnings': admins_earnings, #заработок админов
        'creative_uploads': creative_count, #загруженные креативы
        'community_uploads': community_count, #загруженные сообщества
        'story_views': story_views_count, #просмотры рекламных историй
        'total_error_count': total_error_count, #общий счетчик ошибок
        'owners_count': owners,  # Количество владельцев
        'clients_count': clients,  # Количество заказчиков
    })

# Генерация файла Excel
def generate_excel_file():
    data = [['Date', 'user_count', 'total_visits', 'refill_transactions',
             'withdrawal_transactions', 'Total Revenue', 'admins_earnings',
             'creative_count', 'community_count', 'story_views_count',
             'total_error_count', 'owners_count', 'clients_count',]]

    # Создание книги и листа Excel
    wb = openpyxl.Workbook()
    ws = wb.active

    # Запись данных в лист Excel
    for row_data in data:
        ws.append(row_data)

    # Сохранение книги Excel
    excel_response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    excel_response['Content-Disposition'] = 'attachment; filename=my_data.xlsx'
    wb.save(excel_response)

    return excel_response