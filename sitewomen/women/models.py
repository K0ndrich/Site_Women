from django.db import models
from django.urls import reverse


# определение класа ,который переопределяет objects (Women.objects)
# После создания класса базовый менеджер нельзя использовать етот класс присваиваеться в классе Women
class PublishedManager(models.Manager):
    # функция опеределяет что будет возвращать Women.PublishedManager
    # название get_queryset нельзя изменять
    def get_queryset(self):
        return super().get_queryset().filter(is_published=1)


# создание таблици базы данных. Именно наследование ето делает
class Women(models.Model):
    # создание колонки базы данных. CharField тип данных одна строка
    title = models.CharField(max_length=255)
    # тип данных slug , unique - содержит только уникальные значения для каждой записи
    # db_index - делает индексирование значения, чтоб быстрее выбирать из базы данных
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
    )
    # тип данных часть текста. blank позволяет при создании записи не передавать в колонку значения
    content = models.TextField(blank=True)
    # тип данных дата. auto_now_add записывает время в колонку при создании записи
    time_create = models.DateTimeField(auto_now_add=True)
    # записивыет значение при изменении поля
    time_update = models.DateTimeField(auto_now=True)
    # тип данных bool. default записывает указаное значание, если сами его не передаем
    is_published = models.BooleanField(default=True)

    # сохраняем старый менеджер
    objects = models.Manager()
    # даем название менеджеру класса
    published = PublishedManager()

    # отображение при print(запись в базе)
    def __str__(self):
        return self.title

    # класс в котором переопряделяються сортировки базы данных
    class Meta:
        # переопредиление Women.object.order_by() , выполнение по умолчанию
        ordering = ["-time_create"]
        # устанавливаем индексирования для указаного поля -> ускоряеться поиск записей в базе
        indexes = [
            models.Index(fields=["-time_create"]),
        ]

    # создание адресса url для каждой записи в базе (екзепляри класса Women)
    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})
