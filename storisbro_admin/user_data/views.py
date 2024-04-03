# views.py

from django.shortcuts import render
# from .models import UserProfile
from django.db.models import Sum
from django.utils import timezone

# def user_profile(request):
#     # Фильтрация по дате
#     freshest_profiles = UserProfile.objects.order_by('-registration_date')[:10]
#     oldest_profiles = UserProfile.objects.order_by('registration_date')[:10]

#     # Сумма пополнения, вывода, количество сообществ и креативов
#     replenishment_sum = UserProfile.objects.aggregate(Sum('replenishment_amount'))['replenishment_amount__sum'] or 0
#     withdrawal_sum = UserProfile.objects.aggregate(Sum('withdrawal_amount'))['withdrawal_amount__sum'] or 0
#     community_count_sum = UserProfile.objects.aggregate(Sum('community_count'))['community_count__sum'] or 0
#     creative_count_sum = UserProfile.objects.aggregate(Sum('creative_count'))['creative_count__sum'] or 0

#     context = {
#         'freshest_profiles': freshest_profiles,
#         'oldest_profiles': oldest_profiles,
#         'replenishment_sum': replenishment_sum,
#         'withdrawal_sum': withdrawal_sum,
#         'community_count_sum': community_count_sum,
#         'creative_count_sum': creative_count_sum,
#     }

#     return render(request, 'user_profile.html', context)