from django.contrib import admin, messages

# В етом файле регистрируються модели(таблици) в админ-панель

from .models import Women, Category


# -----   Блок Фильтрации Слева   --------------------------------------------------------------------------------------------------------
# создаем свой один фильтр в блока фильтра слева
class MarriedFilter(admin.SimpleListFilter):
    title = "Статус Женщин"
    # в url адресс вставляеться parameter_name = значение фукнции lookups
    parameter_name = "status"

    # создаем поля для поиска в блоке фильтер слева
    def lookups(self, request, ModelAdmin):
        return [("married", "Замужем"), ("single", "Не замужем")]

    # возвращает отфильтрованные елементы
    def queryset(self, request, queryset):
        # self.value ето значение parameter_name
        if self.value() == "married":
            return queryset.filter(husband__isnull=False)
        else:
            return queryset.filter(husband__isnull=True)


# -----   END   ----------------------------------------------------------------------------------------------------------------------


# регистрация модели вместе с использованием дополнительного класса
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):

    # ---   Внутри Формы Редактирования записи из базы данных   --------------------------------------------------------------------------
    # указываем поля, которые будут отображаться в форме редактирования записи из базы данных
    fields = [
        "title",
        "slug",
        "content",
        "cat",
        "husband",
        "tags",
    ]

    # указывает те поля, которые НЕ будут отображаться в форме редактирования записи из базы данных
    # exclude = ["tags", "is_published"]

    # указывает поля, которые только для чтения
    # readonly_fields = ["slug"]

    # автоматически формируеться slug по записаному нами title , тогда нужно выключать readonly_fields
    prepopulated_fields = {"slug": ("title",)}

    # выводить вторая колонки с вибраними значнеиями колонки tags
    filter_horizontal = [
        "tags",
    ]
    
    # ---   Начальная Форма отображения Базы Данных   ----------------------------------------------------------------------------
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

    # указываем названия колонок по каким будет осуществляться поиск
    # __startwith - будеть искать название только если пишем сначала
    # cat__name - cat ключ связывания таблиц, name - название колонки во второй таблице
    search_fields = (
        "title__startswith",
        "cat__name",
    )

    # указываем колонки по которым будет произваодиться фильтрация -> блок слева
    list_filter = (
        # MarriedFilter - свой созданый више фильтр
        MarriedFilter,
        "cat__name",
        "is_published",
    )

    # создание еще одной колонки в админ панели , ета колонка не связаная с базой данных
    # description дает новое название для колонки
    # ordering связываеться с полем content в базе данных и дает возможность сортировать в админ панеле
    @admin.display(description="Краткое Описание", ordering="content")
    def brief_info(self, women: Women):
        return f"Описание {len(women.content)} символов"

    # ---   Функции для поля Фильтрации которое по Центру   ------------------------------------------------------------------------------------
    # request - запрос до базы данных
    # queryset - набор записей, которы выбрали в админ-панеле в квадратике слева
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


# ----- МОДЕЛЬ CATEGORY -----------------------------------------------------------------------------------------------------------
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    ordering = ["id"]


# Регистрация модели по другому (не используетсья)
# admin.site.register(Women, WomenAdmin)
