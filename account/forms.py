from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import CharField, TextInput, PasswordInput, ModelForm, EmailField, EmailInput, ImageField, FileInput
from .models import Profile


class LoginForm(AuthenticationForm):
    username = CharField(required=True, widget=TextInput(attrs={
        'class': 'form_input',
        'placeholder': 'Логин',
        'autocomplete': 'off',
    }))
    password = CharField(required=True, widget=PasswordInput(attrs={
        'class': 'form_input',
        'placeholder': 'Пароль',
        'autocomplete': 'off',
    }))

    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForm(UserCreationForm):
    username = CharField(required=True, widget=TextInput(attrs={
        'class': 'form_input',
        'placeholder': 'Логин',
        'autocomplete': 'off',
    }))
    password1 = CharField(required=True, widget=PasswordInput(attrs={
        'class': 'form_input',
        'placeholder': 'Пароль',
        'autocomplete': 'off',
    }))
    password2 = CharField(required=True, widget=PasswordInput(attrs={
        'class': 'form_input',
        'placeholder': 'Повторите пароль',
        'autocomplete': 'off',
    }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class EditeProfile(ModelForm):
    first_name = CharField(widget=TextInput(attrs={
        'class': 'form_input',
    }))
    last_name = CharField(widget=TextInput(attrs={
        'class': 'form_input',
    }))
    email = EmailField(widget=EmailInput(attrs={
        'class': 'form_input',
    }))
    avatar = ImageField(widget=FileInput(attrs={
        'class': 'avatar_input',
    }))

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'avatar']