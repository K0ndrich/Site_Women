from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# подключений новой модели, которая создана с помощью унаследования от старой
admin.site.register(User, UserAdmin)
