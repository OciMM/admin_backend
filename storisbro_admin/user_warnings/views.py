from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import WarningToUser
from .serializers import WarningToUserSerializer
from .services import create_user_id, send_message_vk, send_message_email
import requests

