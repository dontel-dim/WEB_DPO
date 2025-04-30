from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Painting
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as AuthLoginView
from django.urls import reverse

class PaintingsView(View):
    """Список (галерея) картин"""
    def get(self, request):
        paintings = Painting.objects.all()
        return render(request, 'paintingapp/painting_list.html', {"painting_list": paintings})

class PaintingDetailView(View):
    """Детали картины"""
    def get(self, request, slug):
        painting = get_object_or_404(Painting, slug=slug)
        return render(request, 'paintingapp/painting_detail.html', {"painting": painting})

class HomeView(View):
    """Главная страница"""
    def get(self, request):
        return render(request, 'paintingapp/home.html')
    
# вход в систему
class LoginView(AuthLoginView):
    template_name = 'paintingapp/login.html'

    def get_success_url(self):
        return reverse('home')
    

class LogoutView(View):
    """Выход из системы"""
    def get(self, request):
        logout(request)
        return redirect('painting_list')  # Перенаправление на главную страницу

class RegisterView(View):
    """Регистрация пользователя"""
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'paintingapp/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('painting_list')
        return render(request, 'paintingapp/register.html', {'form': form})