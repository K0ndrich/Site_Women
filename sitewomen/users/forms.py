from django import forms


# создаем форму входа на сайт не связаную с моделью
class LoginUserForm(forms.Form):
    # widget - указывает каким будет поле для ввода
    username = forms.CharField(
        label="Логин", widget=forms.TextInput(attrs={"class": "form-input"})
    )
    password = forms.CharField(
        label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-input"})
    )
