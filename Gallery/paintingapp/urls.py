from django.urls import path
from . import views
from .views import PaintingsView, PaintingDetailView 

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),  # Страница входа
    path('home/', views.HomeView.as_view(), name='home'),  # Главная страница
    path('painting/<slug:slug>/', views.PaintingDetailView.as_view(), name='painting_detail'),  # Страница для деталей картины
    path('register/', views.RegisterView.as_view(), name='register'),  # Страница регистрации
    path('logout/', views.LogoutView.as_view(), name='logout'),  # Выход
    path('paintings/', views.PaintingsView.as_view(), name='painting_list'),  # Список картин
    path('painting/<slug:slug>/', PaintingDetailView.as_view(), name='painting_detail'),
    
]
