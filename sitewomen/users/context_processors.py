# етот файл хранит контесные процесоры
from women.utils import menu


def get_women_context(request):
    # ключ mainmenu будет передаваться во все шаблоны во всех приложениях нашего проекта
    return {"mainmenu": menu}
