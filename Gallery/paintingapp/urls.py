from django.urls import path
from . import views
from .views import register_view, login_view, logout_view
from .views import PaintingsView, PaintingDetailView, contact_view, artwork_application_view

urlpatterns = [
    path('', login_view, name='login'),  # Страница входа
    path('home/', views.HomeView.as_view(), name='home'),  # Главная страница
    path('painting/<slug:slug>/', views.PaintingDetailView.as_view(), name='painting_detail'),  # Страница для деталей картины
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('paintings/', views.PaintingsView.as_view(), name='painting_list'),  # Список картин
    path('painting/<slug:slug>/', PaintingDetailView.as_view(), name='painting_detail'), # детали картин
    path('contact/', contact_view, name='contact'),
    path('apply/', artwork_application_view, name='artwork_application'),
    
]
