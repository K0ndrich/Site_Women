from django.apps import AppConfig


class WomenConfig(AppConfig):
    # verbose_name содержит название приложения админ панеле
    verbose_name = "Женщины Мира"
    default_auto_field = "django.db.models.BigAutoField"
    name = "women"
