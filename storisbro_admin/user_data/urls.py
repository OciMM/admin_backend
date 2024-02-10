from django.shortcuts import render
from .models import UserProfile

def user_profile(request, user_id):
    user_profile = UserProfile.objects.get(user_id=user_id)
    return render(request, 'user_database/user_profile.html', {'user_profile': user_profile})