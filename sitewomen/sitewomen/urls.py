"""
URL configuration for sitewomen project.

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

from django.contrib import admin
from django.urls import path, include
from women.views import page_not_found

# просписывает главные пути URL на сайте
urlpatterns = [
    # path - указивает путь url , index - название функции которая будет вызиваться
    path("admin/", admin.site.urls),
    # берет url из самого приложения (из указаного в второго файла) http://127.0.0.1:8000/
    path("women/", include("women.urls")),
]
# при ненахождении URL адресса будет вызывать реализованое нами представление page_not_found
handler404 = page_not_found
