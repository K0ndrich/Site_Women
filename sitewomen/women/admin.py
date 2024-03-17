from django.contrib import admin

# В етом файле регистрируються модели(таблици) в админ-панель

from .models import Women

admin.site.register(Women)
