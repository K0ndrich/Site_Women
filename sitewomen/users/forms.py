from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordChangeView , PasswordChangeDoneView

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


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label="Логин", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    password1 = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
    password2 = forms.CharField(
        label="Повтор Пароля", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )

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
            "password1",
            "password2",
        ]

        # переопредиляем названия для наших полей
        labels = {
            "email": "Е-mail",
            "first_name": "Имя",
            "last_name": "Фамилия",
        }
        widgets = {
            "email": forms.TextInput(attrs={"class": "form-input"}),
            "first_name": forms.TextInput(attrs={"class": "form-input"}),
            "last_name": forms.TextInput(attrs={"class": "form-input"}),
        }

    # clean_название поля для проверки значений отдельных полей формы
    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password1"] != cd["password2"]:
            raise forms.ValidationError("Пароли не Совпадают")
        else:
            return cd["password1"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такое E-mail уже существует")
        else:
            return email


class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(
        disabled=True,
        label="Логин",
        widget=forms.TextInput(attrs={"class": "form-input"}),
    )
    email = forms.CharField(
        disabled=True,
        label="E-mail",
        widget=forms.TextInput(attrs={"class": "form-input"}),
    )

    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name"]
        labels = {"first_name": "Имя", "last_name": "Фамилия"}
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-input"}),
            "last_name": forms.TextInput(attrs={"class": "form-input"}),
        }


class UserPasswordChangeForm(forms.ModelForm):
    
