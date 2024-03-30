from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginUserForm

# authenticate функция про аутентификации пользователя -> ищет пользователя по введеным данным
from django.contrib.auth import authenticate, login , logout


def login_user(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            # cleaned_data содержит данные, которые записывал пользователь в поля формы LoginUserForm
            cd = form.cleaned_data
            # authenticate проверяет есть ли переданным данным пользователь в базе
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
    else:
        form = LoginUserForm()
    return render(request, "users/login.html", {"form": form})


def logout_user(request):
    logout(request)
    # users: - ето использование простраства имен из urls.py ( app_name = "users" )
    return HttpResponseRedirect(reverse("users:login"))
