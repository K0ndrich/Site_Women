from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView


class LoginUser(LoginView):

    form_class = LoginUserForm
    template_name = "users/login.html"
    extra_context = {"title": "Авторизация"}

    # def get_success_url(self):
    #     return reverse_lazy("home")


def register(request):
    form = RegisterUserForm()
    return render(request , "users/register.html" , {"form": form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("users:login"))
