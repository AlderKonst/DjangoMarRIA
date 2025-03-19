# Используем официальный образ Python 3.13
FROM python:3.13-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект Django в контейнер
COPY . .

# Указываем VOLUME для медиа-файлов и БД
VOLUME /app/media
VOLUME /app/db.sqlite3

# Указываем порт, который будет использовать приложение
EXPOSE 8000

# Команда для запуска сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]