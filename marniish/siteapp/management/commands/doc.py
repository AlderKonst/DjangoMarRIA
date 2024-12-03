from bs4 import BeautifulSoup # Импорт библиотеки для парсинга HTML
from django.core.management.base import BaseCommand # Импорт базового класса команды Django
from siteapp.models import Document  # Импорт моделей таблицы БД из siteapp

# Здесь будет код для получения данных со страницы Docs.html

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('F:\\UII\\Python+\\DjangoMarRIA\\marniish\\templates\\MarRIA\\Docs.html',
                  'r', encoding='utf-8') as f: # Открываем для чтения html-файл
            content = f.read() # Читаем содержимое файла с кодом
            soup = BeautifulSoup(content, 'html.parser') # Парсим исходный HTML-код
            trs = soup.find_all('tr')[1:] # Извлекаем все tr-теги, кроме первого
            data_before = trs[0] # Извлекаем первый тег
            for tr in trs: # Итерируем по каждому найденному тегу <tr>
                data = tr.find('td', class_='time').get_text() # Извлекаем дату (первый столбец)
                name = tr.find('td', class_='left').get_text()  # Извлекаем название (второй столбец)
                url = tr.find('td').find('a').get('href')  # Извлекаем ссылку (третий столбец)
                if not data: # Если дата публикации пустая
                    Document.objects.get_or_create(name=name, # Название документа
                                            data=data_before,  # Дата публикации документа берётся предыдущий
                                            url=url) # Ссылка его скачивания
                else:
                    Document.objects.get_or_create(name=name,  # Название документа
                                                   data=data,  # Дата публикации документа берётся предыдущий
                                                   url=url)  # Ссылка его скачивания
                    data_before = tr  # Дата публикации документа берётся следующий