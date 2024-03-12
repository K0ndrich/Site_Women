from django import template
from women import views

register = template.Library()


# пользовательский простой тег для шаблонов в html файлах
# name дает новое имя для тега, обращаться нужно по новому имени
@register.simple_tag(name="new_name")
def get_cetegories():
    return views.cats_db


# пользовательский включающий тег для шаблонов
# указаный шаблон возвращает шаблон, return включает переменные в етот указаный шаблон
@register.inclusion_tag("women/list_categories.html")
def show_categories(cat_selected=0):
    cats = views.cats_db
    return {"cats": cats, "cat_selected": cat_selected}
