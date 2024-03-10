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
from django.shortcuts import render, redirect

# reverse записивает в переменую путь с передачей аргументов
from django.urls import reverse

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
        "content": "Биография Анджелины Джоли",
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


# HTTP request - хранить иформацию о текущем запросе от пользователя
def index(request):
    # t = render_to_string("women/index.html")
    # return HttpResponse(t)
    data = {
        "title": "Главная Страница",
        "menu": menu,
        "posts": data_db,
    }
    # 3-й параметр ето значения которые подставляем в шаблон , context можна и не указывать
    return render(request, "women/index.html", context=data)


def about(request):
    data = {
        "title": "Страница About",
    }
    return render(request, "women/about.html", data)


def showpost(request, post_id):
    return HttpResponse(f"Отображение Статьи с ID -> {post_id}")


def addpage(request):
    return HttpResponse("Добавление Статьи")


def contact(request):
    return HttpResponse("Обратная Связь")


def login(request):
    return HttpResponse("Авторизация")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница Не Найдена</h1>")
