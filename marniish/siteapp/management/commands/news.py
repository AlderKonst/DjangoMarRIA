from bs4 import BeautifulSoup # Импорт библиотеки для парсинга HTML
import os # Импорт модуля для работы с ОС
from django.core.files import File # Для работы с файлами в Django
from django.core.management.base import BaseCommand # Импорт базового класса команды Django
from . import site_dir # Импортируем переменную с директорией сайта
from siteapp.models import NewsPicture, NewsBlock, News  # Импорт моделей таблиц БД из siteapp
from datetime import datetime # Для работы со временем

# Здесь будет код для получения данных со страниц News____.html

class Command(BaseCommand):
    def handle(self, *args, **options):
        files = [f for f in os.listdir(site_dir) # Получаем список имён файлов в site_dir
                 if os.path.isfile(os.path.join(site_dir, f)) # Проверяем, является ли элемент файлом, а также
                 and f.lower().startswith('news') # начинается ли имя файла с "news" (независимо от регистра)
                 and f.lower().endswith('.html')] # заканчивается ли имя файла на ".html"
        for file in files: # Перебираем все файлы с новостями
            with open(f'{site_dir}{file}', 'r', encoding='utf-8') as f: # Открываем для чтения каждый html-файл
                content = f.read() # Читаем содержимое файла с кодом
                soup = BeautifulSoup(content, 'html.parser') # Парсим исходный HTML-код
                articles = soup.find_all('article') # Извлекаем все article-теги
                for article in articles: # Итерируем по каждому найденному тегу <article>
                    date_str = article.find('time').get('datetime') # Извлекаем дату события
                    date = datetime.strptime(date_str, '%Y-%m-%d').date()  # Преобразуем строку в дату
                    title = article.find('h3').get_text() # Получаем название события
                    pp = article.find_all('p')  # Извлекаем содержимое из каждого абзаца <p>
                    text = '\n'.join(str(p) for p in pp) # Создаем строку содержимого из всех абзацев <p> блока
                    img = article.find('img') if article.find('img') else '' # Извлекаем изображение, если есть
                    src = img.get('src') if img else '' # Извлекаем путь к изображению, если есть
                    alt = img.get('alt') if img else '' # Извлекаем альт-текст изображения, если есть
                    if img:
                        with open(f'{site_dir}{src}', 'rb') as img_file:
                            Taxon.objects.create(name=taxon, # Создаем объект с таблицей History с текстом
                                                 culture=culture, # Добавляем объект по виду культуры
                                                 text=text, # Добавляем содержимое
                                                 img=File(img_file, name=src), # Передаем файл изображения
                                                 alt=alt) # Добавляем альт-текст изображения
                    else:
                        Taxon.objects.create(name=taxon, # Создаем объект с таблицей History с текстом
                                           culture=culture, # Добавляем объект по виду культуры
                                           text=text, # Добавляем содержимое
                                           img ='',  # Передаем пустой URL
                                           alt = alt)  # Добавляем альт-текст изображения