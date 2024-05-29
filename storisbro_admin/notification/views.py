from django.shortcuts import render, redirect
from .forms import NotificationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import HistoryNotifications
from .serializers import HistoryNotificationsSerializer
from .services import send_message_email, send_message_vk
import requests

def send_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST, request.FILES)
        if form.is_valid():
            notification = form.save()
            if notification.scheduled_time <= timezone.now():
                send_mail(
                    notification.subject,
                    notification.message,
                    settings.DEFAULT_FROM_EMAIL,
                    [notification.user.email],
                    fail_silently=False,
                )
                notification.is_sent = True
                notification.save()
                messages.success(request, 'Уведомление успешно отправлено.')
            else:
                messages.success(request, 'Уведомление запланировано на отправку.')
            return redirect('send_notification')
    else:
        form = NotificationForm()

    return render(request, 'notifications/send_notification.html', {'form': form})



class NotificationToUserAPIView(APIView):
    def get(self, request,):
        notification_model = HistoryNotifications.objects.all()
        serializer = HistoryNotificationsSerializer(notification_model, many=True)
        
        return Response(serializer.data)
    
    def post(
            self, 
            request, 
            message_to_user, 
            message_to_vk, 
            message_to_email, 
            *args, 
            **kwargs
        ):
        data = request.data
        serializer = HistoryNotificationsSerializer(data=data)
        
        if serializer.is_valid():
            # Сохраняем данные
            serializer.save()

            # Получаем пользователя по предоставленному ID
            UID = data.get('UID')  # Предполагается, что user_id передается в запросе
            # user = HistoryNotifications.objects.get(UID=UID)

            """Отправка сообщений через лк"""
            if message_to_user == "true":
                # Получаем данные для обновления из запроса
                data_to_update = {
                    "UID": UID,
                    "title": request.data['title'],
                    "message": request.data['text'],
                }

                # URL для отправки PATCH запроса к API проекта №1 с использованием pk из URL
                url_project1_api = f'http://31.129.96.225/api/notification/send-notification/{UID}/'  # Пример URL для обновления объекта с определенным id

                # Отправка PATCH запроса к API проекта №1
                response = requests.post(url_project1_api, data=data_to_update)

                if response.status_code == 200:
                    # Если запрос успешен, возвращаем сообщение об успешном обновлении
                    return Response({'message': f'Data updated successfully for object with id={UID} in Project 1'})
                else:
                    # Если возникла ошибка, возвращаем соответствующий ответ
                    return Response({'error': f'Failed to update data for object with id={UID} in Project 1'}, status=status.HTTP_400_BAD_REQUEST)
            
            """Отправка сообщений через вк"""
            def get_vk_id_from_project1(uid):
                url = f'http://31.129.96.225/api/notification/send-notification/vk_and_email/{uid}/'
                response = requests.get(url)
                if response.status_code == 200:
                    return response.json().get('vk_id')
                else:
                    return None
                
            if message_to_vk == "true":
                # Отправляем сообщение в VK
                account_vk = get_vk_id_from_project1(UID)
                message_text = data.get('text')
                # account_vk = user.account_vk
                send_message_vk(account_vk, message_text)


            """Отправка сообщений через email"""
            def get_email_from_project1(uid):
                url = f'http://31.129.96.225/api/notification/send-notification/vk_and_email/{uid}/'
                response = requests.get(url)
                if response.status_code == 200:
                    return response.json().get('email')
                else:
                    return None
                
            if message_to_email == "true":
                # Отправляем сообщение по электронной почте
                message_text = data.get('text')
                message_email = get_email_from_project1(UID)
                send_message_email(message_email, message_text)  # Здесь вызываем вашу функцию отправки почты

            return Response({"message": "Данные успешно обработаны"}, status=status.HTTP_200_OK)
            
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)