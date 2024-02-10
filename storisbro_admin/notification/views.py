from django.shortcuts import render, redirect
from .forms import NotificationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils import timezone

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