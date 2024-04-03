from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse
import shutil
import os

from .services import create_zip_of_django_project, download_db

class CreateZIPScript(APIView):
    def get(self, request):
        try:
            create_zip_of_django_project("C:\Admin_Backend_Storisbro\storisbro_admin", )
            return Response({'Успех': 'Функция работает!!!'})
        except Exception as e:
            return Response({'Ошибка': 'Функция не выполняется'})
        

class GetZIPDataBase(APIView):
    def get(self, request):
        # Путь к папке с вашими файлами
        folder_path = r'C:\Admin_Backend_Storisbro\storisbro_admin\backups_zip'
        response = download_db(folder_path)

        return response
