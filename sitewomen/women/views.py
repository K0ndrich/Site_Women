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

from women.models import Women, Category, TagPost

from .forms import AddPostForm

menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить Статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},
]


# HTTP request - хранить иформацию о текущем запросе от пользователя
def index(request):

    # published - ето свой менеджер, которы переопределено от базового
    # select_related - производиться жадная загрузка данных из таблиц по ForeignKey , cat - название колонки связывания с внешней таблицой
    # prefetch_related - производиться жадная загрузка данных из таблиц только по ManyToMany
    # жадная загрузка убирает повторение запросов из баззы данных
    posts = Women.published.all().select_related("cat")

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
    # функция get_object_or_404 либо возвращает обькт по указаным параметрам из модели либо ошибку 404
    # Women - название модели , slug - название колонки из етой модели
    post = get_object_or_404(Women, slug=post_slug)
    data = {
        "title": post.title,
        "menu": menu,
        "post": post,
        "cat_selected": 1,
    }
    return render(request, "women/post.html", data)


def addpage(request):
    if request.method == "POST":
        # request.POST содержит данные атрибут = значение которые были отправленные на сервер
        # is_valid проверяет есть ли правильно переданные ВСЕ значения в форму кроме тех кто required=False, возвращает True - False
        form = AddPostForm(request.POST)
        if form.is_valid():
            # form.cleaned_data возвращает данные, которые вводит пользователь в формы на сайте
            # print(f"{form.cleaned_data}")
            try:
                # создаеться новая запис в базе данных
                # **form.cleaned_data - данные из формы передаються в виде словаря, нужно розпаковывать
                Women.objects.create(**form.cleaned_data)
                return redirect("home")
            except:
                # добавление ошибки в список полей non_field_errors в шаблонах
                form.add_error(None, "Ошибка добавления поста")
    else:
        form = AddPostForm()

    data = {"menu": menu, "title": "Добавление Статьи", "form": form}
    return render(request, "women/addpage.html", data)


def contact(request):
    return HttpResponse("Обратная Связь")


def login(request):
    return HttpResponse("Авторизация")


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk).select_related("cat")
    data = {
        "title": f"Рубрика: {category.name}",
        "menu": menu,
        "posts": posts,
        "cat_selected": category.pk,
    }
    # 3-й параметр ето значения которые подставляем в шаблон , context можна и не указывать
    return render(request, "women/index.html", context=data)


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED)
    data = {
        "title": f"Тег:{tag.tag}",
        "menu": menu,
        "posts": posts,
        "cat_selected": None,
    }
    return render(request, "women/index.html", context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница Не Найдена</h1>")
