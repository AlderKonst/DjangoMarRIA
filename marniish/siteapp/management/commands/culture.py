from bs4 import BeautifulSoup # Импорт библиотеки для парсинга HTML
from django.core.management.base import BaseCommand # Импорт базового класса команды Django
from siteapp.models import CultureGroup, Culture, Taxon  # Импорт моделей таблиц БД из siteapp

# Здесь будет код для получения данных со страниц Grain.html, Grass.html, Jim.html и Potato.html

class Command(BaseCommand):
    def handle(self, *args, **options):
        dir = 'F:\\UII\\Python+\\DjangoMarRIA\\marniish\\templates\\MarRIA\\' # Путь к папке со страницами
        files = {'Grain': 'Зерновые культуры', 'Grass': 'Многолетние травы',
                 'Jim': 'Плодово-ягодные культуры', 'Potato': 'Клубнеплоды'} # Словарь имён html-файлов и группы культур
        for file, group in files.items(): # Итерируем по имени файла сайта и группы агрокультур из списка
            group, _ = CultureGroup.objects.get_or_create(name=group)  # Создаем объект CultureGroup с его названием
            with open(f'{dir}{file}.html', 'r', encoding='utf-8') as f: # Открываем для чтения каждый html-файл
                content = f.read() # Читаем содержимое файла с кодом
                soup = BeautifulSoup(content, 'html.parser') # Парсим исходный HTML-код
                articles = soup.find_all('article')[:-1] # Извлекаем все article-теги, кроме последнего
                for article in articles: # Итерируем по каждому найденному тегу <article>
                    culture = article.find('h3').find('span').get_text() # Извлекаем вид культуры из заголовка
                    culture, _ = Culture.objects.get_or_create(name=culture, # Создаем объект Culture с видом культуры
                                                               group=group) # и своим отношением ко своей группе
                    taxon = article.find('h3').find('b').get_text() # Извлекаем название низшего таксона
                    pp = article.find_all('p')  # Извлекаем содержимое из каждого абзаца <p>
                    text = '\n'.join(str(p) for p in pp) # Создаем строку содержимого из всех абзацев <p> блока
                    img = article.find('img') if article.find('img') else '' # Извлекаем изображение, если есть
                    src = img.get('src') if img else '' # Извлекаем путь к изображению, если есть
                    alt = img.get('alt') if img else '' # Извлекаем альт-текст изображения, если есть
                    Taxon.objects.create(name=taxon, # Создаем объект с таблицей History с текстом
                                         culture=culture, # Добавляем объект по виду культуры
                                         text=text, # Добавляем содержимое
                                         img=src, # Добавляем путь к изображению
                                         alt=alt) # Добавляем альт-текст изображения