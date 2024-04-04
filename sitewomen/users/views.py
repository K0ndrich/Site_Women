from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView


class LoginUser(LoginView):

    form_class = LoginUserForm
    template_name = "users/login.html"
    extra_context = {"title": "Авторизация"}

    # def get_success_url(self):
    #     return reverse_lazy("home")


# представление для регистрации пользователя на основе функции
# def register(request):
#     if request.method == "POST":
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)

#             # шифрует пароль (создает хеш) для указаного новосозданого пользователя
#             user.set_password(form.cleaned_data["password1"])

#             user.save()
#             return render(request, "users/register_done.html")
#     else:
#         form = RegisterUserForm()
#     return render(request, "users/register.html", {"form": form})


# новое представление для регистрации пользователя на основе класса
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register.html"
    extra_context = {"title": "Регистрация"}
    success_url = reverse_lazy("users:login")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:login"))
