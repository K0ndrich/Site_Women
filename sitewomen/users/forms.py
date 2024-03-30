from django import forms
from django.contrib.auth.forms import AuthenticationForm

# get_user_model возвращает тукущую модель user, создан для того чтобы связываться с нею
from django.contrib.auth import get_user_model


# создаем форму входа на сайт не связаную с моделью
# текущий класс унаследуеться от встроеного базового класса формы AuthenticationForm
class LoginUserForm(AuthenticationForm):
    # widget - указывает каким будет поле для ввода
    # username = forms.CharField(
    #     label="Логин", widget=forms.TextInput(attrs={"class": "form-input"})
    # )
    # password = forms.CharField(
    #     label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-input"})
    # )
    class Meta:
        # связываемся с моделью(таблицей) user
        model = get_user_model()
        # указываме какие поля берез из таблици user
        fields = ["username" , "password"]