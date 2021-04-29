import re
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import TextInput, PasswordInput, EmailInput


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=4, label="Введите имя", widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Login'
    }))

    email = forms.CharField(max_length=1000, min_length=4, label="eMail", widget=EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'eMail'
    }))

    password1 = forms.CharField(max_length=1000, min_length=8, label="пароль", widget=PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

    password2 = forms.CharField(max_length=1000, min_length=8, label="повторите пароль", widget=PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Repeat password'
    }))

    def clean_username(self):
        users = User.objects.filter(username=self.cleaned_data['username'])

        if len(users) > 0:
            raise ValidationError('Проверьте правильность данных!')
        return self.cleaned_data['username']

    def clean_email(self):
        result = re.split(r'@', self.cleaned_data['email'])

        if len(result) > 1:
            result2 = re.split(r'\.', result[1])
            if len(result2) > 1:
                return self.cleaned_data['email']
            else:
                raise ValidationError('Введите корректный eMail!')
        else:
            raise ValidationError('Введите корректный eMail!')

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise ValidationError('Пароли не совпали!')
        return self.cleaned_data['password2']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email='a@n.ru',
            password=self.cleaned_data['password1']
        )
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=4, label="Введите логин",
                               widget=TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Логин'
                               }))

    password = forms.CharField(max_length=100, min_length=4, label="Пароль",
                               widget=PasswordInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Пароль'
                               }))

    def clean_username(self):
        users = User.objects.filter(username=self.cleaned_data['username'])

        if len(users) == 0:
            raise ValidationError('Введите корректные данные!')

        return self.cleaned_data['username']