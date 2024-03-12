from django.db import models


# создание таблици базы данных. Именно наследование ето делает
class Women(models.Model):
    # создание колонки базы данных. CharField тип данных одна строка
    title = models.CharField(max_length=255)
    # тип данных slug , unique - содержит только уникальные значения для каждой записи
    # db_index - делает индексирование значения, чтоб быстрее выбирать из базы данных
    slug = models.SlugField(max_length=255, unique=True, db_index=True,)
    # тип данных часть текста. blank позволяет при создании записи не передавать в колонку значения
    content = models.TextField(blank=True)
    # тип данных дата. auto_now_add записывает время в колонку при создании записи
    time_create = models.DateTimeField(auto_now_add=True)
    # записивыет значение при изменении поля
    time_update = models.DateTimeField(auto_now=True)
    # тип данных bool. default записывает указаное значание, если сами его не передаем
    is_published = models.BooleanField(default=True)

    # отображение при print(запись в базе)
    def __str__(self):
        return self.title

    class Meta:
        # переопределяем order_by, по умолчанию будте сортировать по дате создания
        ordering = ["-time_create"]
        # переопределяем Women.objects.all() по полю time_create
        indexes = [models.Index(fields=["-time_create"])]
