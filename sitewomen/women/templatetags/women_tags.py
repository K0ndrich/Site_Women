from django import template
from women import views
from women.models import Category, TagPost
from django.db.models import Count
from women.utils import menu

register = template.Library()

@register.simple_tag()
def get_menu():
    return menu


# пользовательский простой тег для шаблонов в html файлах
# name дает новое имя для тега, обращаться нужно по новому имени
@register.simple_tag(name="new_name")
def get_cetegories():
    return views.cats_db


# пользовательский включающий тег для шаблонов
# указаный шаблон возвращает шаблон, return включает переменные в етот указаный шаблон
@register.inclusion_tag("women/list_categories.html")
def show_categories(cat_selected=0):
    cats = Category.objects.annotate(total=Count("posts")).filter(total__gt=0)
    return {"cats": cats, "cat_selected": cat_selected}


@register.inclusion_tag("women/list_tags.html")
def show_all_tags():
    return {"tags": TagPost.objects.annotate(total=Count("tags")).filter(total__gt=0)}
