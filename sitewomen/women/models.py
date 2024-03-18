from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# менеджер записей -> определение класа , который переопределяет objects (Women.objects)
# После создания класса базовый менеджер нельзя использовать етот класс присваиваеться в классе Women
class PublishedManager(models.Manager):
    # функция опеределяет что будет возвращать Women.published.all()
    # название get_queryset нельзя изменять
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)


# создание таблици (модели) базы данных. Именно наследование от models.Model ето делает
class Women(models.Model):

    # сопоставления - переопредиление значений в текстовые названия , можем использовать ети переменные вместо значений
    class Status(models.IntegerChoices):
        DRAFT = 0, "Черновик"
        PUBLISHED = 1, "Опубликовано"

    # создание колонки базы данных. CharField тип данных одна строка
    # verbose_name содержит название которые будет отображаться в админ панели
    title = models.CharField(max_length=255, verbose_name="Заголовок")

    # тип данных slug , unique - содержит только уникальные значения для каждой записи
    # db_index - делает индексирование значения, чтоб быстрее выбирать из базы данных
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="Slug"
    )
    # тип данных часть текста. blank позволяет при создании записи не передавать в колонку значения
    content = models.TextField(blank=True, verbose_name="Текс Статьи")

    # тип данных дата. auto_now_add записывает время в колонку при создании записи
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время Создания")

    # записивыет значение при изменении поля
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время Изменения")

    # тип данных bool. default записывает указаное значание, если сами его не передаем
    # choices - используем переопредиление имен
    is_published = models.BooleanField(
        choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
        default=Status.DRAFT,
        verbose_name="Возможность Публикации",
    )

    # сохраняем старый менеджер. При создании нового нужно сохранять старый
    objects = models.Manager()
    # даем название менеджеру класса
    published = PublishedManager()

    # создаеться новая колонка, которая соответствует колонке в таблице Category -> отношение многие к одному
    # Category - указывает на какую таблицу(модель) будем ссылаться
    # CASCADE - при удаление записи Category удалеться и запись в Women
    # PROTECT - запрещает удаление записи в Category, если запись ссылаеться на Women
    # related_name - указывает названия для менеджера записей для Category
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, related_name="posts")

    # создание отношения многие ко многим
    tags = models.ManyToManyField("TagPost", blank=True, related_name="tags")

    # создание отношение один к одному
    # SET_NULL если удалем значения во второй таблице Husband, тогда в таблице Women устанавливаеться значение Null
    husband = models.OneToOneField(
        "Husband",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="wuman",
    )

    # отображение при print(запись в базе)
    def __str__(self):
        return self.title

    # класс в котором переопряделяються сортировки базы данных
    class Meta:
        # verbose_name содержит название для текущей модели(таблици) в панеле администратора в одном числе
        verbose_name = "Известные Женщины"

        # verbose_name содержит название для текущей модели(таблици) в панеле администратора в множественном числе
        verbose_name_plural = "Известные Женщины"

        # при получении списка с записями базы данных вывод сортировать по значению колонки time_create
        ordering = ["-time_create"]

        # устанавливаем индексирования для указаного поля -> ускоряеться поиск записей в базе
        indexes = [
            models.Index(fields=["-time_create"]),
        ]

    # создание адресса url для каждой записи в базе (екзепляри класса Women)
    # post - ето name из urls.py
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})

    # переопредиляем кнопку сохранить в добавлении записи в базу данных
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# создание второй таблички (модели) -> многие к одному
# при удаление значений записи в Сategory возможно удаление записи в Women
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Имя")
    slug = models.SlugField(max_length=255, unique=False, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    # метод get_absolute_url также добавляет кнопку смотреть на сайте в админ-панели
    def get_absolute_url(self):
        # category - ето name из urls.py
        # self.slug - беретьcя значение колонки slug из записи в базе данных
        return reverse("category", kwargs={"cat_slug": self.slug})


# создание третей таблици для отношения многие ко многим
class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse("tag", kwargs={"tag_slug": self.slug})


class Husband(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    m_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name
