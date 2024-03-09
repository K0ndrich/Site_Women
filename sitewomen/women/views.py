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

#  from django.shortcuts import render

# render_to_string  позволяет работать с шаблонами (не рекомендуеться)
from django.template.loader import render_to_string


# HTTP request - хранить иформацию о текущем запросе от пользователя
def index(request):
    # t = render_to_string("women/index.html")
    # return HttpResponse(t)
    return render(request, "women/index.html")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>This id -> {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    # request.GET содержит ключи и значения параметров GET запроса
    print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>This text -> {cat_slug} </p>")


def archive(request, year):
    if year > 2023:

        # Http404 выводит преставление которое мы передали в handler404 в sitewomen/urls.py
        # raise Http404()

        # reverse записывает путь в переменую, также указывает аргументы для пути URL
        uri = reverse("cats", args=("music",))
        # перенаправление на страницу по указаному URL , если if возвращает True
        # permanent=True код состояние 302, а если False код состояние 301 (постоянное перемищение)

        # return redirect(uri, permanent=False) == HttpResponseRedirect(uri)
        return redirect(uri, permanent=True)  # == HttpResponsePermanentRedirect(uri)

    return HttpResponse(f"<h1>Статьи по категориям</h1><p>This year -> {year}</p>")

def about(request):
    return render(request,"women/about.html")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>function --> page_not_found</h1>")
