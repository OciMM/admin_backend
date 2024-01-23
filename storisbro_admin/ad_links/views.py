from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import AdLinkModel
from .serializers import AdLinkModelSerializer
from .services import generate_ad_link


class AdLinkModelAPIView(APIView):
    def get(self, request):
        link_model = AdLinkModel.objects.all()
        serializer = AdLinkModelSerializer(link_model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # Используем сериализатор для валидации данных
        serializer = AdLinkModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Генерация реферальной ссылки
        ad_link = generate_ad_link()

        # Сохранение объекта в базе данных
        AdLinkModel.objects.create(
            name=serializer.validated_data['name'],
            link=ad_link
        )

        return Response({"message": "Рекламная ссылка успешно создана"}, status=status.HTTP_201_CREATED)
    

class AdLinkClickView(APIView):
    def get(self, request, link):
        ad_link = get_object_or_404(AdLinkModel, link=link)
        ad_link.clicks += 1
        ad_link.save()
        return Response({"message": "Успешный переход по рекламной ссылке"}, status=status.HTTP_200_OK)