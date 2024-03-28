# Внутри етого файла храняться Миксины для использования их в представлениях внутри views.py

menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить Статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},
]


# DataMixin - Миксин для сборки данных, которые вставляються в шаблон
class DataMixin:
    # пререопределяем extra_context
    extra_context = {}
    title_page = None
    cat_selected = None

    def __init__(self):
        if self.title_page:
            self.extra_context["title"] = self.title_page

        if "menu" not in self.extra_context:
            self.extra_context["menu"] = menu

        if self.cat_selected is not None:
            self.extra_context["cat_selected"] = self.cat_selected

    # context - ето словарь c данными для вставки в шаблон из функции get_context_data
    def get_mixin_context(self, context, **kwargs):
        context["menu"] = menu
        context["cat_selected"] = None
        # kwargs = {"key":1} пример передачи словаря
        context.update(kwargs)
        return context
