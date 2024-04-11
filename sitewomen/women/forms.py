# Внутри файла вписываються классы Forms , чтоб быстро создать екзпеляры етого класса в templates / file.html
from django import forms
from .models import Category, Husband, Women

# добавление других валидаторов для проверки значений, которые ввел пользователь
from django.core.validators import MinLengthValidator, MaxLengthValidator, BaseValidator

from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError


# свой валидатор для проверки вписаного текста в поле формы
@deconstructible
class RussianValidator:
    ALLOWED_CHARS = (
        "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "
    )
    code = "russian"

    def __init__(self, message=None):
        self.message = (
            message
            if message
            else "Должни присутствовать только русские символы, дефис и пробел"
        )

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


class AddPostForm(forms.ModelForm):
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

    class Meta:
        model = Women
        fields = [
            "title",
            "slug",
            "content",
            "photo",
            "is_published",
            "cat",
            "husband",
            "tags",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-input"}),
            "content": forms.Textarea(attrs={"cols": 50, "rows": 5}),
        }
        labels = {"slug": "URL"}

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) > 50:
            raise ValidationError("Длина превышает 50 символов")

        return title


class UploadFileForm(forms.Form):
    file = forms.ImageField(label="Картинка")
