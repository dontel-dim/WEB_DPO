from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Painting
from django.contrib.auth import login, authenticate, logout
from .forms import ContactForm, ArtworkApplicationForm, UserRegistrationForm, UserLoginForm


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
    

def contact_view(request): # форма обратной связи
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.clean_message()
            return render(request, 'paintingapp/contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'paintingapp/contact.html', {'form': form})


def artwork_application_view(request): # подача зааявок
    if request.method == 'POST':
        form = ArtworkApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.clean() 
            return render(request, 'paintingapp/application_success.html')
    else:
        form = ArtworkApplicationForm()
    
    return render(request, 'paintingapp/artwork_application.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Вход после регистрации
            return redirect('home') 
    else:
        form = UserRegistrationForm()
    
    return render(request, 'paintingapp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Переход к главной странице или другой
    else:
        form = UserLoginForm()
    
    return render(request, 'paintingapp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')