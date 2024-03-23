# Внутри файла вписываються классы Forms , чтоб быстро создать екзпеляры етого класса в templates / file.html
from django import forms
from .models import Category, Husband

# добавление других валидаторов для проверки значений, которые ввел пользователь
from django.core.validators import MinLengthValidator, MaxLengthValidator

# добавляет возможность создавать пользовательские валидаторы
from django.utils.deconstruct import deconstructible

# добавление исключения валидации
from django.core.exceptions import ValidationError


# Создание пользовательского свого валидатора для проверки введеных значений
@deconstructible
class RussianValidator:
    ALLOWED_CHARS = (
        "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "
    )
    code = "russian"

    # создание екзепляра нашого класса(самого валидатора)
    def __init__(self, message=None):
        self.message = (
            message
            if message
            else "Должни присутствовать только русские символы, дефис и пробел"
        )

    # вызов валидатора (работа проверки) после записи значений пользователем
    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


# клас для автоматического создания форм
class AddPostForm(forms.Form):
    # label дает свое название для колонки на сайте
    title = forms.CharField(
        max_length=255,
        min_length=5,
        # label дает свое название для колонки на сайте
        label="Заголовок",
        # ипользуем свой пользовательский валидатор (пока не нужно)
        # validators=[RussianValidator()],
        # widget позволяет указывать свои значения атрибутам указаного тега, значения не будут изменяться в шаблонах
        # самостоятельно указываем свои атрибути , они не будут изменяться при их использовании в шаблонах
        widget=forms.TextInput(attrs={"class": "form-input"}),
        error_messages={
            # передаем значения, которые будут записываться значения
            "min_length": "Слишком короткий заголовок",
            "required": "Без заголовка никак",
        },
    )

    slug = forms.SlugField(
        max_length=255,
        label="URL",
        # validator позволяет создавать свою проверку записаного текста пользователем в полля ввода
        # message определя текс, который будет возвращать form.errors
        validators=[
            MinLengthValidator(5, message="Минимум 5 символов"),
            MaxLengthValidator(100, message="Максимум 100 символов"),
        ],
    )

    # required позволяет указывать нужно ли заполнять поле или нет
    content = forms.CharField(
        widget=forms.Textarea(attrs={"cols": 50, "rows": 5}),
        required=False,
        label="Контент",
    )
    # initial указывает начальное значение
    is_published = forms.BooleanField(initial=True, label="Статус")
    # поля хранят выподающий список из всех значений моделей Category , Husband
    cat = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Категория не Выбрана",
        label="Категории",
    )
    husband = forms.ModelChoiceField(
        queryset=Husband.objects.all(),
        required=False,
        empty_label="Не замужем",
        label="Муж",
    )

    # создаем валидатор, который можно не вписывать в поле формы при создании
    # clean__название поля к которому применяем валидатор
    def clean_title(self):
        title = self.cleaned_data["title"]
        ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "
        if not (set(title) <= set(ALLOWED_CHARS)):
            raise ValidationError(
                "Должни присутствовать только русские символы, дефис и пробел"
            )
