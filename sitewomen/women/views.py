from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    Http404,
    HttpResponseRedirect,
    HttpResponsePermanentRedirect,
)
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from .models import Women, Category, TagPost, UploadFiles
from .forms import AddPostForm, UploadFileForm
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
from .utils import DataMixin
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class WomenHome(DataMixin, ListView):

    template_name = "women/index.html"

    context_object_name = "posts"

    title_page = "Главная Старница"

    cat_selected = 0

    def get_queryset(self):
        return Women.published.all().select_related("cat")


@login_required(login_url="/admin/")
def about(request):

    contact_list = Women.published.all()

    paginator = Paginator(contact_list, 3)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)
    return render(
        request, "women/about.html", {"title": "О сайте", "page_obj": page_obj}
    )


class ShowPost(DataMixin, DetailView):
    template_name = "women/post.html"

    slug_url_kwarg = "post_slug"

    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context["post"].title)

    def get_object(self, queryset=None):
        return get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwarg])


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    title_page = "Добавление Статьи"
    template_name = "women/addpage.html"
    success_url = reverse_lazy("home")
    login_url = "/women/"
    def form_valid(self,form):
        # commit = False означает что не нжно ничего записывать в новосозданую запись в модели
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class UpdatePage(DataMixin, UpdateView):
    model = Women
    fields = ["title", "slug", "content", "photo", "is_published", "cat"]
    success_url = reverse_lazy("home")
    template_name = "women/addpage.html"
    title_page = "Редактирование Статьи"


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


class WomenCategory(DataMixin, ListView):

    template_name = "women/index.html"
    context_object_name = "posts"

    allow_empty = False

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        cat = context["posts"][0].cat
        return self.get_mixin_context(
            context, title="Категория - " + cat.name, cat_selected=cat.pk
        )

    def get_queryset(self):
        return Women.published.filter(cat__slug=self.kwargs["cat_slug"]).select_related(
            "cat"
        )


class TagPostList(DataMixin, ListView):

    template_name = "women/index.html"
    context_object_name = "posts"
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        tag = TagPost.objects.get(slug=self.kwargs["tag_slug"])
        self.get_mixin_context(context, title="Тег - " + tag.tag, menu=menu)

        return context

    def get_queryset(self):

        return Women.published.filter(
            tags__slug=self.kwargs["tag_slug"]
        ).select_related("cat")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница Не Найдена</h1>")
