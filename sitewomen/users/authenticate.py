from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model


# переопредиляем класс аутентификации
class EmailAuthBackend(BaseBackend):
    # сама аутентификация пользователя
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()

        try:
            user = user_model.objects.get(email=username)
            # проверяте пароль на совпадение с етим пользователем в базе
            if user.check_password(password):
                return user
            else:
                return None
        except (user_model.DoesNotExist, user_model.MultipleObjectsReturned):
            return None

    # полeчение пользователя для сайта(создание сесии) после аутентификации
    def get_user(self, user_id):
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
