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
    path("", views.index),
    # int: конвертер преобразовывает значение строки от пользователя url в тип int
    # car_id название переменной
    path("cats/<int:cat_id>/", views.categories),
    # slug принимает любое слово в url
    path("cats/<slug:cat_slug>/", views.categories_by_slug),
    # принимает число длиной только в 4 символа, котрое состоит из цивт от 0 до 9
    # имеет приоритет выполение више
    # re_path(r"^archive/(?P<year>[0-9]{4})/$", views.archive),
    # используем свой конвертор
    path("archive/<year4:year>/", views.archive),
]
