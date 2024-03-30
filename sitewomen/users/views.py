from django.shortcuts import render
from django.urls import reverse , reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginUserForm

# authenticate функция про аутентификации пользователя -> ищет пользователя по введеным данным
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
# СТАРОЕ представление авторизации пользователя на сайте
# def login_user(request):
#     if request.method == "POST":
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             # cleaned_data содержит данные, которые записывал пользователь в поля формы LoginUserForm
#             cd = form.cleaned_data
#             # authenticate проверяет есть ли переданным данным пользователь в базе
#             user = authenticate(
#                 request, username=cd["username"], password=cd["password"]
#             )
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse("home"))
#     else:
#         form = LoginUserForm()
#     return render(request, "users/login.html", {"form": form})


# НОВОЕ представление для авторизации пользователя на сайте основанное на клессе
class LoginUser(LoginView):
    
    # form_class содержит обьект, котоырй будет подставляться в form (login.html)    
    # нельзя использовать LoginUserForm , если он не унаследован от AuthenticationForm
    form_class = LoginUserForm 
    template_name = "users/login.html"
    extra_context = {"title": "Авторизация"}
    
    # def get_success_url(self):
    #     return reverse_lazy("home")


def logout_user(request):
    logout(request)
    # users: - ето использование простраства имен из urls.py ( app_name = "users" )
    return HttpResponseRedirect(reverse("users:login"))
