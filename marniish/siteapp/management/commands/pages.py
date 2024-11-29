import os # Импорт модуля для работы с ОС
from bs4 import BeautifulSoup # Импорт библиотеки для парсинга HTML
from django.core.management.base import BaseCommand # Импорт базового класса команды Django
#from siteapp.models import Page # Импорт модели таблицы БД Page из siteapp
from pprint import pprint

# Здесь будет код для получения данных со всех страниц сайта марниисх.рф

#class Command(BaseCommand):
#    def handle(self, *args, **options):
dir = f'F:\\ДОКИ\\Python+\\DjangoMarRIA\\marniish\\templates\\MarRIA\\' # Директория поиска html-файлов
pages = [page for page in os.listdir(dir)
         if page.endswith('.html')] # Перебираем страницы и сохраняем в генереторе имена файлов с .html в конце
for page in pages:
    with open(os.path.join(f'{dir}{page}'), 'r', encoding='utf-8') as f:  # Прочитываем каждый html-файл
        content = f.read()  # Читаем содержимое файла c кодом
        soup = BeautifulSoup(content, 'html.parser')  # Парсим исходный HTML-код
        title = soup.find('title').get_text()[:-72] # Получаем уникальную часть текста титульника
        description = soup.select_one('meta[name="description"]')['content'] # Получаем описание страницы
        parent = soup.find('li', class_ = 'index')
#        if soup['parent_url']:
#            parent = Page.objects.get(url=soup['parent_url'])
        pprint(parent)
