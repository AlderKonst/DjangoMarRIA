import os # Для работы с ОС
from bs4 import BeautifulSoup # Импорт библиотеки для парсинга HTML
from django.core.management.base import BaseCommand # Импорт базового класса команды Django
#from siteapp.models import HistoryData, History # Импорт моделей таблиц БД HistoryData, History из siteapp

# Здесь будет код для получения данных со страницы Article.html

#class Command(BaseCommand):
#    def handle(self, *args, **options):
with open(f'F:\\ДОКИ\\Python+\\DjangoMarRIA\\marniish\\templates\\MarRIA\\About.html',
          'r', encoding='utf-8') as f:  # Открываем для чтения нужный файл
    content = f.read()  # Читаем содержимое файла c кодом
    soup = BeautifulSoup(content, 'html.parser')  # Парсим исходный HTML-код
    articles = soup.find_all('article')[2:]  # Находим все теги <article> (первые 2 не надо)
    for article in articles:
        year = article.find('h3').get_text()[:4]
        day_month = article.find('b')
        if day_month:
            day_month = day_month.get_text()
        print(year, day_month)