# Dokerfile - файл хранит сценарий действий для работы с контейнером

# унаследуем основу из другого Dokerfile для нашего Doker Image (Докер Образ)
FROM python:3.12.2

# устанавливаем постоянные переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

# задает рабочую текущую локальную директорию для выполнения команд RUN и CMD
WORKDIR /Projects/My_Site/sitewomen

# копируем файл с зависимостями из локального проекта в doker image
COPY ./req.txt /Projects/My_Site/sitewomen/req.txt

# RUN - выполняет команды, котоыре попадают doker image , еще до запуска контейнера
# устанавливаем зависимости(стороние библиотеки) для нашего проекта на сервере
RUN pip install -r /Projects/My_Site/sitewomen/req.txt

# копируем весь проект в текущую директорию
# . - означает текущая директория на сервере
COPY . /Projects/My_Site/sitewomen

# указываем порт, который будем использовать
EXPOSE 8000

# CMD - выполняет команды в CMD уже после запуска контейнера
# запускаем проект на сервере
# CMD ["python" ,"manage.py", "migrate"]
# CMD ["python","manage.py","runserver","0.0.0.0:8000"]
