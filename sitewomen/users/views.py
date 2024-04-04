from django.db.models import QuerySet
from django.db.models.base import Model as Model
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from .forms import (
    LoginUserForm,
    RegisterUserForm,
    ProfileUserForm,
    UserPasswordChangeForm,
)
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import (
    LoginView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView


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


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = "users/profile.html"
    extra_context = {"title": "Профиль Пользователя"}

    def get_success_url(self):
        return reverse_lazy("users:profile")
        # return reverse_lazy("users:profile", args=[self.request.user.pk])

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"

class UserPasswordChangeDone(PasswordChangeDoneView):
    template_name = "users/password_change_done.html"
    title = "Пароль успешно изменен"

    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:login"))
