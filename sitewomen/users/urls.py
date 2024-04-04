# Внутри етого файла храняться пути для авторизации пользователя
from django.urls import path
from . import views

# даем название своему пространству имен
app_name = "users"
urlpatterns = [
    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.RegisterUser.as_view(), name="register"),
]
