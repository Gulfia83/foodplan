from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Like

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class AvatarForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['avatar']
