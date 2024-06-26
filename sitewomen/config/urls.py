"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from config import settings
from django.contrib import admin
from django.urls import path, include
from women.views import page_not_found
from django.conf.urls.static import static

# просписывает главные пути URL на сайте
urlpatterns = [
    # path - указивает путь url , index - название функции которая будет вызиваться
    path("admin/", admin.site.urls),
    # авторизация пользователя
    # namespace="users" береться уникальное пространство имен,которое храниться в url.py в переменной app_name
    # пространстов служит для создание уникального пути не связаного с другими путями с аналогичными названиями
    path("users/", include("users.urls", namespace="users")),
    # берет url из самого приложения (из указаного в второго файла) http://127.0.0.1:8000/
    path("women/", include("women.urls")),
    # берез из django debug toolbar
    path("__debug__/", include("debug_toolbar.urls")),
]

# связывает между собой пути MEDIA_URL + MEDIA_ROOT для нормального отображения файлов.
# нужно прописивать при использовании сервера в режиме ОТЛАДКИ
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# при ненахождении URL адресса будет вызывать реализованое нами представление page_not_found
handler404 = page_not_found

# содержит название панели администратора
admin.site.site_header = "Панель Администрирования"
# содержит название второго заголовка ниж
admin.site.index_title = "Извесные Женщины Мира"
