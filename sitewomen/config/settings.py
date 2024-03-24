"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-xx3$)(x8a^=!+=h#6=$-ud5^1jz7gjt7xv(%%39%&z+=krfdh5"

# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG режим сайта.При ненахождении URL адресса , если True не позволяет выкинуть ошибку 404
# При ненахождении URL адресса , если False повзволяет выкинуть ошибку 404
DEBUG = True

# разрешенные host адреса , указываем наш локальный host
ALLOWED_HOSTS = ["127.0.0.1"]
# добавление для django-debug-toolbar
INTERNAL_IPS = ["127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    # покдлючение админ-панели
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    # позволяет подключать статические файлы к проекту
    "django.contrib.staticfiles",
    # регистрация созданого приложения с названием women. Путь ->  women/apps/WomenConfig
    "women.apps.WomenConfig",
    # добавление сторонего пакета с разширениями
    "django_extensions",
    # добавление django debug toolbar
    "debug_toolbar",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "config.urls"

# настройка для шаблонизатора
TEMPLATES = [
    {
        # указываем имя для шаблонизатора
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # повзлояет прописывать  пути для файлов шаблонов
        "DIRS": [BASE_DIR / "templates"],
        # True - ищет по умолчанию шаблоны в config/women/templates/women/index.html
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        # драйвер для взаемодействия с базой данных
        "ENGINE": "django.db.backends.sqlite3",
        # разположение базы данных в проекте
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# указываем общий язык для всего нашего проекта
# LANGUAGE_CODE = "en-us"  - англиский
LANGUAGE_CODE = "ru-RU"  # - русский

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


# базовый путь к статическим файлам
STATIC_URL = "static/"


# содержит нестандарные пути для папки static , из которой будут файлы перемещаться в главную папку STATIC_ROOT указаную више
# в нашем случае содержит статические файлы для адмни панели
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
# MEDIA_ROOT указывать путь к медиа файла, которые загрузил пользователь на сайт
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")


# содержит в путь в главной папки с статическими фалами, куда перемещаються после python manage.py collectstatic
# STATIC_ROOT = ""


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
