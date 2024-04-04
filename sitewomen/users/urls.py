# Внутри етого файла храняться пути для авторизации пользователя
from django.urls import path
from . import views
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)


# даем название своему пространству имен
app_name = "users"
urlpatterns = [
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("password-change", views.UserPasswordChange.as_view(), name="password-change"),
    path(
        "password-change/done",
        views.UserPasswordChangeDone.as_view(),
        name="password_change_done",
    ),
    # процес отправки письма на e-mail для смены пароля
    path(
        "password_reset",
        PasswordResetView.as_view(template_name="users/password_reset_form.html"),
        name="password_reset",
    ),
    # при успешной отправки письма на e-mail для смены пароля
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),
    # изменение пароля после, того как пользователь получил письмо
    path(
        # <uidb64>/<token> взяты из документации
        "password_reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    # успешное изменение пароля, полсе того как пользователь получил письмо
    path(
        "password_reset/complete/",
        PasswordResetCompleteView.as_view(
            template_name="users/password_reset_coplete.html"
        ),
        name="password_reset_complete",
    ),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("profile/", views.ProfileUser.as_view(), name="profile"),
]
