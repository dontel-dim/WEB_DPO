from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Ваше имя')
    email = forms.EmailField(required=True, label='Ваш Email')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Сообщение')

class ArtworkApplicationForm(forms.Form):
    artwork_title = forms.CharField(max_length=200, required=True, label='Название картины')
    artwork_description = forms.CharField(widget=forms.Textarea, required=True, label='Описание картины')
    price = forms.DecimalField(decimal_places=2, max_digits=10, required=True, label='Цена (в рублях)')
    artwork_image = forms.ImageField(required=True, label='Изображение картины')
    phone_number = forms.CharField(max_length=15, required=True, label='Номер телефона')
    artist_name = forms.CharField(max_length=100, required=True, label='Имя художника')
    artist_age = forms.IntegerField(required=True, label='Возраст художника')
    artist_description = forms.CharField(widget=forms.Textarea, required=True, label='Описание художника')
    artist_photo = forms.ImageField(required=True, label='Фотография художника')