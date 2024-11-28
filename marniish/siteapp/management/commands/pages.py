import os # Импорт модуля для работы с ОС
from bs4 import BeautifulSoup # Импорт библиотеки для парсинга HTML
from django.core.management.base import BaseCommand # Импорт базового класса команды Django
from siteapp.models import PageWay, Page # Импорт моделей таблиц БД PageWay и Page из siteapp

# Здесь будет код для получения данных со всех страниц сайта марниисх.рф

class Command(BaseCommand):
    def handle(self, *args, **options):
        pages = [page for page in os.listdir(os.path.join('templates', 'MarRIA'))
                 if page.endswith('.html')] # Перебираем страницы и сохраняем в генереторе имена файлов с .html в конце
        for page in pages:
            with open(os.path.join('templates', 'MarRIA', page), 'r', encoding='utf-8') as f:  # Прочитываем каждый html-файл
                content = f.read()  # Читаем содержимое файла c кодом
                soup = BeautifulSoup(content, 'html.parser')  # Парсим исходный HTML-код