# позволяет давать ответы на запросы пользователя по URL
from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    Http404,
    HttpResponseRedirect,
    HttpResponsePermanentRedirect,
)

# redirect перенаправляет на другую страницу с другим url
# render позволяет работать с шаблонами и отправлять на страницу
from django.shortcuts import render, redirect, get_object_or_404

# reverse записивает в переменую путь с передачей аргументов
from django.urls import reverse

from women.models import Women

menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить Статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},
]

data_db = [
    {
        "id": 1,
        "title": "Анджелина Джоли",
        "content": """<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.
        Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».""",
        "is_published": True,
    },
    {
        "id": 2,
        "title": "Марго Робби",
        "content": "Биография Марго Робби",
        "is_published": False,
    },
    {
        "id": 3,
        "title": "Джулия Робертс",
        "content": "Биография Джулия Робертс",
        "is_published": True,
    },
]

cats_db = [
    {"id": 1, "name": "Актрисы"},
    {"id": 2, "name": "Певици"},
    {"id": 3, "name": "Спортсменки"},
]


# HTTP request - хранить иформацию о текущем запросе от пользователя
def index(request):
    # published - ето свой менеджер, которы переопределено от базового
    posts = Women.published.all()
    data = {
        "title": "Главная Страница",
        "menu": menu,
        "posts": posts,
        "cat_selected": 0,
    }
    # 3-й параметр ето значения которые подставляем в шаблон , context можна и не указывать
    return render(request, "women/index.html", context=data)


def about(request):
    data = {
        "title": "Страница About",
    }
    return render(request, "women/about.html", {"title": "О сайте", "menu": menu})


def showpost(request, post_slug):
    # функция get_object_or_404 либо возвращает обьека по указаным параметрам из модели либо ошибку 404
    post = get_object_or_404(Women, slug=post_slug)
    data = {
        "title": post.title,
        "menu": menu,
        "post": post,
        "cat_selected": 1,
    }
    return render(request, "women/post.html", data)


def addpage(request):
    return HttpResponse("Добавление Статьи")


def contact(request):
    return HttpResponse("Обратная Связь")


def login(request):
    return HttpResponse("Авторизация")


def show_category(request, cat_id):
    data = {
        "title": "Отображение по рубрикам",
        "menu": menu,
        "posts": data_db,
        "cat_selected": cat_id,
    }
    # 3-й параметр ето значения которые подставляем в шаблон , context можна и не указывать
    return render(request, "women/index.html", context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница Не Найдена</h1>")
