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
    # name позволяет использовать заданый маршрут в других файлах проекта
    # использование представления на основе класса
    path(
        "",
        # значения extra_context из views.py можно переопределять здесь
        views.WomenHome.as_view(),
        name="home",
    ),
    path("about/", views.about, name="about"),
    path("addpage/", views.AddPage.as_view(), name="add_page"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),
    path("post/<slug:post_slug>/", views.showpost, name="post"),
    path("category/<slug:cat_slug>/", views.WomenCategory.as_view(), name="category"),
    path("tag/<slug:tag_slug>/", views.show_tag_postlist, name="tag"),
]
