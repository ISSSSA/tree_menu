FROM python:3.11-slim
LABEL authors="Воронов Игорь"

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию для приложения
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения в контейнер
COPY . /app/

# Собираем статику
#RUN python manage.py collectstatic --noinput

# Открываем порт 8000 для доступа к приложению
EXPOSE 8000

# Устанавливаем переменные окружения для Django
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Выполняем миграции перед запуском приложения
RUN python manage.py migrate
RUN python manage.py fill_db

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]