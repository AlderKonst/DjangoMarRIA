from .models import Page # Импорт модели Page для работы с данными страниц

def page_info(request): # Определение контекстного процессора для получения информации о странице
    page_url = request.resolver_match.url_name # Получаем имя URL-шаблона из текущего запроса
    if page_url == 'Newses': # Проверяем, является ли URL-шаблон 'Newes' (особый случай для страницы новостей)
        page_url = 'News_last' # Если да, используем 'News_last' как URL для страницы новостей
    if page_url: # Проверяем, что page_url не пустой
        try: # Пробуем
            page = Page.objects.get(url=page_url) # получить объект Page по URL
            return {'page': page} # Возвращаем объект page в контекст
        except Page.DoesNotExist: # Если возникла ошибка, где Page не найден
            return {'page': None} # то возвращаем None в контекст
    return {'page': None}  # Если page_url пустой, то возвращаем None в контекст