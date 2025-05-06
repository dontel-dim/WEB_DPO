from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    """Middleware для защиты маршрутов от неавторизованных пользователей."""
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Если пользователь не авторизован
        if not request.user.is_authenticated:
            if request.path == reverse('home'):
                return redirect('login')
        
        return response     
    