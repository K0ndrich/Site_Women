# ета файл создан для того чтоб брать urls из етого приложения
from django.urls import path, re_path, register_converter

# точка . - означает импортирование из текущей директории
from . import views

# импортируем файл где реализуем свои конвекторы
from . import converters

# подлючение своего конвертора из импортированого више файла
# year4 даем название для своего конвертора
register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    # name позволяет использовать заданый маршрут в других файлах проекта обращаясь по его значению
    # использование представления WomenHome на основе класса
    path(
        "",
        # значения extra_context можна указывать вручную в .as_view(extra_context = {"title":"Главная Страница"})
        views.WomenHome.as_view(),
        name="home",
    ),
    path("about/", views.about, name="about"),
    path("addpage/", views.AddPage.as_view(), name="add_page"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),
    # название post_slug переопределено из slug (колонка в модели Women) в slug_url_kwarg (views.py)
    path("post/<slug:post_slug>/", views.ShowPost.as_view(), name="post"),
    path("category/<slug:cat_slug>/", views.WomenCategory.as_view(), name="category"),
    path("tag/<slug:tag_slug>/", views.TagPostList.as_view(), name="tag"),
    path("edit/<slug:slug>/", views.UpdatePage.as_view(), name="edit_page"),
    path("delete/<slug:slug>/", views.DeletePage.as_view(), name="delete"),
]
