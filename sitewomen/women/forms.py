from django import forms
from .models import Category, Husband


# клас для автоматического создания форм
class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    # widget позволяет точнее указывать тип поля для ввода
    # required позволяет указывать нужно ли заполнять поле или нет
    content = forms.CharField(widget=forms.Textarea, required=False)
    is_published = forms.BooleanField()
    # поля хранят выподающий список из всех значений моделей Category , Husband
    cat = forms.ModelChoiceField(
        queryset=Category.objects.all(), empty_label="Виберите"
    )
    husband = forms.ModelChoiceField(
        queryset=Husband.objects.all(), empty_label="Виберите"
    )
