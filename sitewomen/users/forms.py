from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


class LoginUserForm(AuthenticationForm):

    username = forms.CharField(
        label="Логин", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    password = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )

    class Meta:
        model = get_user_model()
        fields = ["username", "password"]


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Повтор Пароля", widget=forms.PasswordInput())

    # Meta класс в формах служит для связивания с моделью в какую мы будем записывать данные
    class Meta:
        # связываемся с моделью user
        model = get_user_model()
        # указяваем поля, которые будут отобраться в нашей форме (см. Документация -> Использование системы аутентификации Django)
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "password2",
        ]
        # переопредиляем названия для наших полей
        labels = {
            "username": "UserName",
            "email": "Е-mail",
            "first_name": "Имя",
            "last_name": "Фамилия",
            "password": "Пароль",
            "password2": "Повтор Пароля",
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Пароли не Совпадают")
        else:
            return cd["password"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().filter(email=email).exists():
            raise forms.ValidationError("Такое e-mail уже существует")
        else:
            return email
