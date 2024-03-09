# позволяет давать ответы на запросы пользователя по URL
from django.http import HttpResponse, HttpResponseNotFound

#  from django.shortcuts import render

# Create your views here.


# HTTP request - хранить иформацию о текущем запросе от пользователя
def index(request):
    return HttpResponse("Страница приложения women")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>This id -> {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    # request.GET содержит ключи и значения параметров GET запроса
    print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>This text -> {cat_slug} </p>")


def archive(request, year):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>This year -> {year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>hello my friend</h1>")
