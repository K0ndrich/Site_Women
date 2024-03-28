# Внутри етого файла храняться Миксины для использования их в представлениях внутри views.py

menu = [
    {"title": "О сайте", "url_name": "about"},
    {"title": "Добавить Статью", "url_name": "add_page"},
    {"title": "Обратная связь", "url_name": "contact"},
    {"title": "Войти", "url_name": "login"},
]


# DataMixin - Миксин для сборки данных, которые всталвяються в шаблон
class DataMixin:
    # context - ето словарь c данными для вставки в шаблон из функции get_context_data
    def get_mixin_context(self, context, **kwargs):
        context["menu"] = menu
        context["cat_selected"] = None
        # kwargs = {"key":1} пример передачи словаря
        context.update(kwargs)
        return context
