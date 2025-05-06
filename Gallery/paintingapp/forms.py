from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
import re

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Этот адрес электронной почты уже используется.')
        return email


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Ваше имя')
    email = forms.EmailField(required=True, label='Ваш Email')
    message = forms.CharField(max_length=200, min_length=10, widget=forms.Textarea, required=True, label='Сообщение')

class ArtworkApplicationForm(forms.Form):
    artwork_title = forms.CharField(max_length=200, min_length=2, required=True, label='Название картины')
    artwork_description = forms.CharField(max_length=200, min_length=10, widget=forms.Textarea, required=True, label='Описание картины')
    price = forms.DecimalField(decimal_places=2, max_digits=10, required=True, label='Цена (в рублях)')
    artwork_image = forms.ImageField(required=True, label='Изображение картины')
    phone_number = forms.CharField(max_length=15, required=True, label='Номер телефона')
    artist_name = forms.CharField(max_length=100, required=True, label='Имя художника')
    artist_age = forms.IntegerField(required=True, label='Возраст художника')
    artist_description = forms.CharField(max_length=200, min_length=10, widget=forms.Textarea, required=True, label='Описание художника')
    artist_photo = forms.ImageField(required=True, label='Фотография художника')

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        if not re.match(r'^\+?\d{11,15}$', phone):
            raise ValidationError('Введите корректный номер телефона.')
        return phone

    def clean_artist_age(self):
        age = self.cleaned_data['artist_age']
        if age < 10 or age > 120:
            raise ValidationError('Возраст художника должен быть от 10 до 120 лет.')
        return age

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError('Цена должна быть положительной.')
        return price