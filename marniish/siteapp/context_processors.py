from django.shortcuts import get_object_or_404 # Импорт функции для получения объекта или вызова 404 ошибки
from .models import Page # Импорт модели Page для работы с данными страниц

def page_info(request): # Определение контекстного процессора для получения информации о странице
    page_url = request.resolver_match.url_name # Получаем имя URL-шаблона из текущего запроса
    if page_url == 'News': # Проверяем, является ли URL-шаблон 'News' (особый случай для страницы новостей)
        page_url = 'Newses' # Если да, используем 'Newses' как URL для страницы новостей
    if page_url: # Проверяем, что page_url не пустой
        try: # Пробуем
            page = get_object_or_404(Page, url=page_url) # получить объект Page по URL
            return {'page': page} # Возвращаем объект page в контекст
        except: # Если возникла ошибка (например, Page не найден)
            return {'page': None} # Возвращаем None в контекст
    return {'page': None}  # Если page_url пустой, возвращаем None в контекст