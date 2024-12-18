import os # Импорт модуля для работы с ОС
from bs4 import BeautifulSoup # Импорт библиотеки для парсинга HTML
from django.core.management.base import BaseCommand # Импорт базового класса команды Django
from . import site_dir # Импортируем переменную с директорией сайта
from siteapp.models import Page # Импорт модели таблицы БД Page из siteapp

# Здесь будет код для получения данных со всех страниц сайта марниисх.рф

class Command(BaseCommand):
    def handle(self, *args, **options):
        pages = [page for page in os.listdir(site_dir)
                 if page.endswith('.html')] # Перебираем страницы и сохраняем в генереторе имена файлов с .html в конце
        for page in pages:
            with open(os.path.join(site_dir, page), 'r', encoding='utf-8') as f:  # Прочитываем каждый html-файл
                content = f.read()  # Читаем содержимое файла c кодом
                soup = BeautifulSoup(content, 'html.parser')  # Парсим исходный HTML-код
                title = soup.find('title').get_text()[:-72] # Получаем уникальную часть текста титульника
                description = soup.select_one('meta[name="description"]')['content'] # Получаем описание страницы
                parent_block = soup.find('li', class_ = 'parent') # Получаем блок, указывающий на родительскую страницу
                url = '' # Инициируем адрес текущей страницы пустым
                parent_url = '' # Инициируем адрес родительской страницы пустым
                parent_title = '' # Инициируем имя родительской страницы пустым
                if parent_block: # Если блок родительской страницы есть
                    parent_url = parent_block.find('a').get('href') # Получаем адрес родительской страницы
                    parent_title = parent_block.find('a').get_text() # Получаем имя родительской страницы

                    def format_url(url): # В страницах новостей убирает .html и форматирует в таком виде: News/ГГГГ
                        url = url[:-5] # Убираем .html из имени файла
                        if url.startswith('News'): # Если адрес начинается с News
                            year = url[4:] # Извлекаем год из имени страницы
                            return f"News/{year}" # Форматируем URL как News/ГГГГ
                        else: # Если адрес не начинается с News (остальные)
                            return url # Возвращаем адрес страницы без .html

                    url = format_url(page) # Убираем .html из имени текущей страницы с таким (News/ГГГГ) форматом
                    parent_url = format_url(parent_url) # Убираем .html из адреса родительской страницы с таким (News/ГГГГ) форматом
                Page.objects.get_or_create( # Создаем объект таблицы БД Page
                    title=title,  # Создаем поле именем страницы
                    url = url, # Создаем поле адреса текущей страницы без расширения
                    description = description, # Создаем поле описания страницы
                    parent_url = parent_url, # Создаем поле адреса родительской страницы без расширения
                    parent_title = parent_title # Создаем поле имени родительской страницы
                    )