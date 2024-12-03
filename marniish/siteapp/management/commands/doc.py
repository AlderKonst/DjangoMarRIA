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
            time = [tr.find('td', class_='time').get_text(strip=True) if tr.find('td', class_='time') else '' for tr in trs] # Извлекаем даты
            data_before = time[0] # Дата публикации документа берётся первая
            for n, tr in enumerate(trs): # Итерируем по каждому найденному тегу <tr>
                data = time[n] # Извлекаем дату
                name = tr.find('td', class_='left').get_text(strip=True)  # Извлекаем название (второй столбец)
                url = tr.find('a').get('href')  # Извлекаем ссылку (третий столбец)
                if not data: # Если дата публикации пустая
                    Document.objects.get_or_create(name=name, # Название документа
                                            data=data_before,  # Дата публикации документа берётся предыдущий
                                            url=url) # Ссылка его скачивания
                else:
                    Document.objects.get_or_create(name=name,  # Название документа
                                                   data=data,  # Дата публикации документа берётся предыдущий
                                                   url=url)  # Ссылка его скачивания
                    data_before = data  # Дата публикации документа берётся следующий