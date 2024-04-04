# Внутри етого файла храняться пути для авторизации пользователя
from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView


# даем название своему пространству имен
app_name = "users"
urlpatterns = [
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("password-change", PasswordChangeView.as_view(), name="password-change"),
    path(
        "password-change/done",
        PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("profile/", views.ProfileUser.as_view(), name="profile"),
]
