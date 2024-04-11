from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
import datetime


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
        label="Логин",
        validators=[],
        widget=forms.TextInput(attrs={"class": "form-input"}),
    )
    password1 = forms.CharField(
        label="Пароль",
        validators=[],
        widget=forms.PasswordInput(
            attrs={"class": "form-input"},
        ),
    )
    password2 = forms.CharField(
        label="Повтор Пароля",
        validators=[],
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
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
    # поля, которые мы создаем самостоятельно
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
    this_year = datetime.date.today().year
    # будет показываться поле для указания даты рождения с указаным диапазоном range
    date_birth = forms.DateField(
        widget=forms.SelectDateWidget(
            years=tuple(range(this_year - 100, this_year - 5))
        )
    )

    class Meta:
        model = get_user_model()
        # поля, которые будут выводиться на текущей странице
        fields = ["photo", "username", "email", "date_birth", "first_name", "last_name"]
        labels = {"first_name": "Имя", "last_name": "Фамилия"}
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-input"}),
            "last_name": forms.TextInput(attrs={"class": "form-input"}),
        }


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Старый Пароль", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )

    new_password1 = forms.CharField(
        label="Новый Пароль", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )

    new_password2 = forms.CharField(
        label="Подтверждение Пароля",
        widget=forms.PasswordInput(attrs={"class": "form-input"}),
    )
