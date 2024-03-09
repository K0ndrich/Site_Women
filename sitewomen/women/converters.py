# ето файл созда для реализации конвертеров для url
class FourDigitYearConverter:
    regex = "[0-9]{4}"

    # преобразовывает в тип int
    def to_python(self, value):
        return str(value)

    def to_url(self, value):
        return "%04d" % value
