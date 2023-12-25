from django.contrib.auth.forms import AuthenticationForm
from django import forms

from users.models import User
class UserLoginForm(AuthenticationForm):
    class Meta:
        username = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите имя пользователя'
        }))

        password = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control py-4',
            'placeholder': 'Введите пароль'
        }))

        model = User
        fields = ('username', 'password')