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
from django.urls import reverse, reverse_lazy

from .models import Women, Category, TagPost, UploadFiles

from .forms import AddPostForm, UploadFileForm

# добавляем представления на основе классов
from django.views import View
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)

# добавляем свой миксин из файла с миксинами utils.py
from .utils import DataMixin

menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить Статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},
]


# -----   СТАРОЕ ПРЕДАСТАВЛЕНИЕ index основаное на одной функции , новое представление ↓↓↓↓↓   ----------------------------------------------------------------------------------------
# HTTP request - хранить иформацию о текущем запросе от пользователя
# def index(request):

#     # published - ето свой менеджер, которы переопределено от базового
#     # select_related - производиться жадная загрузка данных из таблиц по ForeignKey , cat - название колонки связывания с внешней таблицой
#     # prefetch_related - производиться жадная загрузка данных из таблиц только по ManyToMany
#     # жадная загрузка убирает повторение запросов из баззы данных
#     posts = Women.published.all().select_related("cat")

#     data = {
#         "title": "Главная Страница",
#         "menu": menu,
#         "posts": posts,
#         "cat_selected": 0,
#     }
#     # 3-й параметр ето значения которые подставляем в шаблон , context можна и не указывать
#     return render(request, "women/index.html", context=data)
# -----   END   ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# -----   Реализация представление на основе класса TemplateView (переопредиляем представление index)   ------------------------------------------------------
# class WomenHome(TemplateView):
#     # внутри не нужно прописывать render, само связывает шаблон и данные для шаблона
#     template_name = "women/index.html"

#     # внутрь extra_context передаються статические данные в момент загрузки сайта.
#     # Из get_context_data могут передаваться внутрь extra_context уже динамические данные
#     extra_context = {
#         "title": "Главная Страница",
#         "menu": menu,
#         "posts": Women.published.all().select_related("cat"),
#         "cat_selected": 0,
#     }

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Главная Страница"
#         context["menu"] = menu
#         context["posts"] = Women.published.all().select_related("cat")
#         # позволяет подставлять cat_id в URL пользователем
#         context["cat_selected"] = int(self.request.GET.get("cat_id", 0))
#         return context

# -----   END   --------------------------------------------------------------------------------------------------------------------------------------------------------


# представление WomenHome (переопределен index) на основе класса ListView
class WomenHome(DataMixin, ListView):
    # указываем модель из которой будут браться записи , связываем представление в моделью
    # ListView фомирует внутри указаного шаблона object_list, в которой храняться наши записи из модели уканаой више
    template_name = "women/index.html"

    # даем новое название для object_list в index.html или других файлах .html
    context_object_name = "posts"

    title_page = "Главная Старница"

    cat_selected = 0

    # вместо extra_context используем метод Миксина
    # extra_context = {
    #     "title": "Главная Страница",
    #     "menu": menu,
    #     "cat_selected": 0,
    # }

    # в классе ListView можна выбирать записи из базы данных
    # берем записи из базы данных для вывода, ети записи будуть находиться внутри object_list в index.html
    # model = Women значение переопредиляеться внутри етой функции
    def get_queryset(self):
        return Women.published.all().select_related("cat")


# НЕ ИСПОЛЬЗУЕМ старая версия для ↓↓↓↓↓
# функция для загрузки файлов от пользователя на сервер (функция взяли из сайта документации)
# f - ето файл, который передал пользователь
# def handle_uploaded_file(f):
#     # нужно указать путь куда будем сохранять файл + создать папку с первым названием в файла проекта(не приложения)
#     with open(f"uploads/{f.name}", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


# просто реализовуваем добавление данных в модель UploadFiles
def about(request):
    if request.method == "POST":
        # создание заполненого обьекта формы, которая заполнена колекцией запроса пользователя(request.POST)
        # и файлом, который отправил пользователь
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            # НЕ ИСПОЛЬЗУЕМ
            # передаем внутрь функции обьявленой више файл, который отправил пользователь
            # handle_uploaded_file(form.cleaned_data["file"])
            # --------------------------------------------------------------------------

            # file ето значение name в классе UploadFileForm в forms.py
            # создаем запись в модели UploadFiles
            fp = UploadFiles(file=form.cleaned_data["file"])
            fp.save()
    else:
        # создание обьекта формы , который пустой
        form = UploadFileForm()

    data = {
        "title": "О сайте",
        "menu": menu,
        "form": form,
    }
    return render(request, "women/about.html", data)


# СТАРОЕ представление для отображение одного поста на основе функции ----------------------------------------------------------------------------------------
# def showpost(request, post_slug):
#     # функция get_object_or_404 либо возвращает обькт по указаным параметрам из модели либо ошибку 404
#     # Women - название модели , slug - название колонки из етой модели
#     post = get_object_or_404(Women, slug=post_slug)
#     data = {
#         "title": post.title,
#         "menu": menu,
#         "post": post,
#         "cat_selected": 1,
#     }
#     return render(request, "women/post.html", data)
# -----   END   ------------------------------------------------------------------------------------------------------------------------------


# НОВОЕ представление для показа одного поста основаное на классе DetailView
# DetailView позволяет брать и отображать одну запись из модели
# DataMixin - ето миксин который хранит внутри себя информацию для заполнения в шаблонах ,
# Миксины всегда записываються первыми , перед класами представления
class ShowPost(DataMixin, DetailView):
    # не нужно , если используем get_object
    # model = Women
    template_name = "women/post.html"

    # указываем название переменной которая будет подставляться в URL (urls.py)
    slug_url_kwarg = "post_slug"

    # внутрь post.html педедаеться обьекта object который хранит значения model = Women
    # context_object_name дает новое название для обьекта object внутри post.html
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # берем метод из миксина
        return self.get_mixin_context(context, title=context["post"].title)

    # функция из которой беруться записи и записываються в object в post.html , название object переопределено на post
    def get_object(self, queryset=None):
        return get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwarg])


# -----   СТАРОЕ ПРЕДСТАВЛЕНИЕ ADDPAGE основанное на одной функции -------------------------------------------------------------------------
# def addpage(request):
#     if request.method == "POST":
#         # request.POST содержит данные атрибут = значение которые были отправленные на сервер
#         form = AddPostForm(request.POST, request.FILES)
#         # is_valid проверяет соответствуют ли передание значения характеристикам, которые указаны в forms.py
#         if form.is_valid():
#             # form.cleaned_data возвращает данные, которые вводит пользователь в формы на сайте
#             # print(f"{form.cleaned_data}")
#             # try:
#             #     # создаеться новая запис в базе данных
#             #     # **form.cleaned_data - данные из формы передаються в виде словаря, нужно розпаковывать
#             #     Women.objects.create(**form.cleaned_data)
#             #     return redirect("home")
#             # except:
#             #     # добавление ошибки в список полей non_field_errors в шаблонах
#             #     form.add_error(None, "Ошибка добавления поста")

#             # данные записанные пользователем в форме -> записиваються в базу данных Women
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()

#     data = {"menu": menu, "title": "Добавление Статьи", "form": form}
#     return render(request, "women/addpage.html", data)
# -----   END   ---------------------------------------------------------------------------------------------------------------------------------


# # Представление ADDPAGE основаное на классе View   ----------------------------------------------------------------------------------------
# # View позволяет отображать страници в зависимости от запроса GET или POST пользователя
# class AddPage(View):
#     def get(self, request):
#         form = AddPostForm()
#         data = {"menu": menu, "title": "Добавление Сатьи", "form": form}
#         return render(request, "women/addpage.html", data)

#     def post(self, request):
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("home")
#         data = {"menu": menu, "title": "Добавление Сатьи", "form": form}
#         return render(request, "women/addpage.html", data)
# -----   END   ---------------------------------------------------------------------------------------------------------------------------------


# предсталвение AddPage основаное на классе DetailView   -----------------------------------------------------------------------------
# DetailView позволяет работать с формами и переопредилять их методы
# class AddPage(FormView):

#     # form_class ccылаеться на класс формы (forms.py)
#     # передает обьект form в addpage.html
#     form_class = AddPostForm
#     template_name = "women/addpage.html"

#     # после успешной отправки формы перенаправляемся по указаному URL
#     # reverse возвращает полный путь URL сразу при запуске сайта
#     # reverse_lazy возвращает полный путь URL только при ее вызове
#     success_url = reverse_lazy("home")
#     extra_context = {"title": "Добавление Статьи", "menu": menu}

#     # form_valid функция сохранения данных из формы в модель , ета функция вызываеться после проверки is_valid()
#     # form - ето текущая форма которую отправил пользователь , определяеться в form_class = AddPostForm
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
# -----   END   --------------------------------------------------------------------------------------------------------------


# Представление AddPage основанное на классе CreateView
# CreateView класс для создание новых записей в модели
class AddPage(DataMixin, CreateView):
    form_class = AddPostForm

    # model = Women
    # отображение всех полей из формы , также можна указывать каждое поле
    # fields = "__all__"
    title_page = "Добавление Статьи"
    template_name = "women/addpage.html"
    success_url = reverse_lazy("home")

    # функция form_valid уже по умолчанию работает внутри CreateView , запись автоматически сохраняеться в модель
    # после выполнение представление выполняеться get_absolute_url в модели, которая привязана Women -->
    # и после успешного добавлние поста переходит на етот пост на сайте


# представление для изменение уже существующих постов на основе класса UpdateView
# UpdateView влужит для изменения уже существующих записей в модели
class UpdatePage(DataMixin, UpdateView):
    model = Women
    fields = ["title", "slug", "content", "photo", "is_published", "cat"]
    success_url = reverse_lazy("home")
    template_name = "women/addpage.html"
    title_page = "Редактирование Статьи"


# представление для удаления постов на основе класса UpdateView
# DeleteView служит для удаление записей из модели
class DeletePage(DataMixin, DeleteView):
    model = Women
    fields = ["title", "slug", "content", "photo", "is_published", "cat"]
    success_url = reverse_lazy("home")
    template_name = "women/addpage.html"
    title_page = "Удаление Статьи"


def contact(request):
    return HttpResponse("Обратная Связь")


def login(request):
    return HttpResponse("Авторизация")


# -----   СТАРОЕ ПРЕДСТАВЛЕНИЕ ПОКАЗЫВАНИЯ КАТЕГОРИЯ СЛЕВА основаное на функции   ---------------------------------
# def show_category(request, cat_slug):
#     category = get_object_or_404(Category, slug=cat_slug)
#     posts = Women.published.filter(cat_id=category.pk).select_related("cat")
#     data = {
#         "title": f"Рубрика: {category.name}",
#         "menu": menu,
#         "posts": posts,
#         "cat_selected": category.pk,
#     }
#     # 3-й параметр ето значения которые подставляем в шаблон , context можна и не указывать
#     return render(request, "women/index.html", context=data)
# ------   END   -----------------------------------------------------------------------------------------


# НОВОЕ представление показа постов по категориям show_category на основе класса ListView
# ListView позволяет отображать все записи в модели
class WomenCategory(DataMixin, ListView):

    template_name = "women/index.html"
    context_object_name = "posts"

    # добавляем что , при пустом значении context["posts"] будет генерироваться ошибка 404
    allow_empty = False

    # get_context_data соберает все значение динамических данных(которые отправил пользователь) -->
    # в extra_contex , который передаеться внутрь шаблона указаного в template_name
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # берем из всех записей модели Women значение колонки cat
        cat = context["posts"][0].cat
        return self.get_mixin_context(
            context, title="Категория - " + cat.name, cat_selected=cat.pk
        )

        # context["title"] = "Категория - " + cat.name

        # # cat_selected атрибут который можна вписать в url cat_selected=1 , ети значения из колонки id модели Category
        # # cat_selected - ето значение из колонки cat в модели Women
        # context["cat_selected"] = cat.pk
        # return context

    def get_queryset(self):
        # self.kwargs["cat_slug"] ето значение которое мы передали в URL (название переменной определяеться в urls.py)
        return Women.published.filter(cat__slug=self.kwargs["cat_slug"]).select_related(
            "cat"
        )


# СТАРОЕ ПРЕДСТАВЛЕНИЕ show_tag_postlist основаное на функции   -------------------------------------------------------------------------
# def show_tag_postlist(request, tag_slug):
#     tag = get_object_or_404(TagPost, slug=tag_slug)
#     posts = tag.tags.filter(is_published=Women.Status.PUBLISHED)
#     data = {
#         "title": f"Тег:{tag.tag}",
#         "menu": menu,
#         "posts": posts,
#         "cat_selected": None,
#     }
#     return render(request, "women/index.html", context=data)
# -----   END   ------------------------------------------------------------------------------------------------------------------------------------


# НОВОЕ ПРЕДСТАВЛЕНИЕ показа постов по тегам от show_tag_postlist основанное на классе ListView
class TagPostList(DataMixin,ListView):

    template_name = "women/index.html"
    context_object_name = "posts"
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # self.kwargs["tag_slug"] ето значение которое мы передали в URL (название переменной определяеться в urls.py)
        tag = TagPost.objects.get(slug=self.kwargs["tag_slug"])
        self.get_mixin_context(context , title ="Тег - " + tag.tag , menu = menu  )

        return context

    def get_queryset(self):

        # tags__slug   tags ето название колонки в модели Women , slug ето название колонки модели на которою ссылаеться tags
        return Women.published.filter(
            tags__slug=self.kwargs["tag_slug"]
        ).select_related("cat")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница Не Найдена</h1>")
