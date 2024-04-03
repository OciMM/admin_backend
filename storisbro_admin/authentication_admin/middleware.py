from django.http import HttpResponseForbidden

class AllowIPMiddleware:
    allowed_ips = ['194.187.249.170']

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_ip = '194.187.249.170'

        if user_ip not in self.allowed_ips:
            return HttpResponseForbidden("Доступ запрещен")

        response = self.get_response(request)
        return response