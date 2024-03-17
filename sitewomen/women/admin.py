from django.contrib import admin, messages

# В етом файле регистрируються модели(таблици) в админ-панель

from .models import Women, Category


# регистрация модели вместе с использованием дополнительного класса
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):

    # содержит название колонок, которые будут отображаться
    list_display = (
        "title",
        "time_create",
        "is_published",
        "cat",
        "brief_info",
    )

    # содержит названия колокнок нажавши на которые переходит в выбраную запись в базе
    list_display_links = ("title",)

    # сортировка сначала по первому, если есть одинаковые тогда по второму
    ordering = ["-time_create", "title"]

    # позволяет редакторовать значения в указаной колонке
    list_editable = (
        "is_published",
        "cat",
    )

    # указываме максимальное количество статей который будут отображаться сразу при входе
    list_per_page = 5

    # указывает названия функции с помощью которых можна взаемодействовать с записями в базе данных
    actions = ("set_published", "set_draft")

    # создание еще одной колонки в админ панели , ета колонка не связаная с базой данных
    # description дает новое название для колонки
    # ordering связываеться с полем content в базе данных и дает возможность сортировать в админ панеле
    @admin.display(description="Краткое Описание", ordering="content")
    def brief_info(self, women: Women):
        return f"Описание {len(women.content)} символов"

    # request - запрос до базы данных
    # queryset - набор записей, которы выбрали в админ-панеле
    @admin.action(description="Опубликовать Выбраные Записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        # показывает инофрмацию више(оповещение) после выполнения текущей функции
        self.message_user(request, f"Изменено {count} записей")

    @admin.action(description="Снять с Публикации")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        # messages.WARNING показывает оранжеми оповещение про изменении
        self.message_user(request, f"Изменено {count} записей", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    ordering = ["id"]


# Регистрация модели по другому
# admin.site.register(Women, WomenAdmin)
