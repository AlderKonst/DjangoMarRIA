import os # Для работы с OC
from bs4 import BeautifulSoup # Импорт библиотеки для парсинга HTML
import logging # Импорт библиотеки для логирования
from . import site_dir # Импортируем переменную с директорией сайта
from django.core.management.base import BaseCommand # Импорт базового класса команды Django
from siteapp.models import TrendBasic # Импорт модели таблицы БД TrendBasic из siteapp

# Здесь будет код для получения свойств полезных ссылок из index.html и style.css

class Command(BaseCommand):
    def handle(self, *args, **options):
        dir_html = os.path.join(site_dir, 'Trend.html') # Директория c Trend.html

        with open(dir_html, 'r', encoding='utf-8') as f: # Прочитываем html-файл
            content = f.read() # Читаем содержимое файла c кодом
            soup = BeautifulSoup(content, 'html.parser') # Парсим исходный HTML-код
            ol = soup.find('ol') # Получаем блок с нумерованным списком
            lis = ol.find_all('li') # Получаем все пункты списка
            for li in lis: # Перебираем все ссылки
                text = li.get_text()  # Получаем текст из пункта списка
                TrendBasic.objects.get_or_create(name=text) # Текст из пункта списка добавляем, если ещё нет