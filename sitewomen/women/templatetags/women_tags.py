from django import template
from women import views

register = template.Library()


# простой тег для шаблонов в html файлах
@register.simple_tag
def get_cetegories():
    return views.cats_db


# включающий тег для шаблонов , возвращает шаблон, return включает переменные в етот шаблон
@register.inclusion_tag("women/list_categories.html")
def show_categories(cat_selected=0):
    cats = views.cats_db
    return {"cats": cats, "cat_selected": cat_selected}
