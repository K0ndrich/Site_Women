# позволяет давать ответы на запросы пользователя по URL
from django.http import HttpResponse, HttpResponseNotFound, Http404

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
    if year > 2023:
        # Http404 выводит преставление которое мы передали в handler404 в sitewome/urls.py
        raise Http404()

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>This year -> {year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>function --> page_not_found</h1>")
