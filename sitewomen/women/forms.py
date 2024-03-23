from django import forms
from .models import Category, Husband

# Внутри файла вписываються классы Forms , чтоб быстро создать екзпеляры етого класса в templates / file.html


# клас для автоматического создания форм
class AddPostForm(forms.Form):
    # label дает свое название для колонки на сайте
    title = forms.CharField(
        max_length=255,
        label="Заголовок",
        # widget позволяет указывать свои значения атрибутам указаного тега, значения не будут изменяться в шаблонах
        # самостоятельно указываем свои атрибути , они не будут изменяться при их использовании в шаблонах
        widget=forms.TextInput(attrs={"class": "form-input"}),
    )
    slug = forms.SlugField(max_length=255, label="URL")
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
