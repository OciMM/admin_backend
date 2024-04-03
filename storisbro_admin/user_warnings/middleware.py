from django.utils import timezone
# from .models import CustomUser


# class CheckBlockedStatusMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Получаем текущего пользователя (если он аутентифицирован)
#         user = request.user if request.user.is_authenticated else None

#         # Проверяем статус блокировки перед выполнением запроса
#         if user and user.is_active:
#             user.check_block_status()

#         response = self.get_response(request)

#         return response
