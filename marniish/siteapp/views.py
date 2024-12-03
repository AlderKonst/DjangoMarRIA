from django.shortcuts import (render, # Импортируем функцию для рендеринга шаблонов,
                              get_object_or_404, # получения объекта или возврата 404 ошибки
                              HttpResponseRedirect) # и перенаправления
from django.urls import reverse # Импортируем функцию для получения URL по имени
from django.core.mail import send_mail # Импортируем функцию для отправки электронной почты
# Импортируем модели соответствующих таблиц
from .models import (Page, TrendItem, Reference, Article, Progress, History,
                     HistoryData, Culture, Taxon, CultureGroup)  # Импортируем модели соответствующих таблиц

def index(request): # Для рендеринга главной страницы
    page = Page.objects.get(url='index') # Получаем запись в таблице Page с именем index в поле url
    trends = TrendItem.objects.all() # Получаем все записи в таблице TrendItem
    references = Reference.objects.all() # Получаем все записи в таблице Reference
    context = {'page': page, 'trends': trends, 'references': references} # Передаем поля в шаблон
    return render(request, 'siteapp/index.html', context) # Рендерим шаблон с передачей в него переменной page

def news2024(request): # Для рендеринга страницы новостей за 2024 год
    page = Page.objects.get(url='News2024') # Получаем запись в таблице Page с именем News2024 в поле url
    context = {'page': page} # Передаем шаблон
    return render(request, 'siteapp/News2024.html', context) # Рендерим шаблон с передачей в него переменной page

def news2023(request): # Для рендеринга страницы новостей за 2023 год
    page = Page.objects.get(url='News2023') # Получаем запись в таблице Page с именем News2023 в поле url
    context = {'page': page} # Передаем шаблон
    return render(request, 'siteapp/News2023.html', context) # Рендерим шаблон с передачей в него переменной page

def news2022(request): # Для рендеринга страницы новостей за 2022 год
    page = Page.objects.get(url='News2022') # Получаем запись в таблице Page с именем News2022 в поле url
    context = {'page': page} # Передаем шаблон
    return render(request, 'siteapp/News2022.html', context) # Рендерим шаблон с передачей в него переменной page

def news2021(request): # Для рендеринга страницы новостей за 2021 год
    page = Page.objects.get(url='News2021') # Получаем запись в таблице Page с именем News2021 в поле url
    context = {'page': page} # Передаем шаблон
    return render(request, 'siteapp/News2021.html', context) # Рендерим шаблон с передачей в него переменной page

def news2020(request): # Для рендеринга страницы новостей за 2020 год
    page = Page.objects.get(url='News2020') # Получаем запись в таблице Page с именем News2020 в поле url
    context = {'page': page} # Передаем шаблон
    return render(request, 'siteapp/News2020.html', context) # Рендерим шаблон с передачей в него переменной page

def news2019(request): # Для рендеринга страницы новостей за 2019 год
    page = Page.objects.get(url='News2019') # Получаем запись в таблице Page с именем News2019 в поле url
    context = {'page': page} # Передаем шаблон
    return render(request, 'siteapp/News2019.html', context) # Рендерим шаблон с передачей в него переменной page

def news2018(request): # Для рендеринга страницы новостей за 2018 год
    page = Page.objects.get(url='News2018') # Получаем запись в таблице Page с именем News2018 в поле url
    context = {'page': page} # Передаем шаблон
    return render(request, 'siteapp/News2018.html', context) # Рендерим шаблон с передачей в него переменной page

def news2017(request): # Для рендеринга страницы новостей за 2017 год
    page = Page.objects.get(url='News2017') # Получаем запись в таблице Page с именем News2017 в поле url
    context = {'page': page} # Передаем шаблон
    return render(request, 'siteapp/News2017.html', context) # Рендерим шаблон с передачей в него переменной page

def news2016(request): # Для рендеринга страницы новостей за 2016 год
    page = Page.objects.get(url='News2016') # Получаем запись в таблице Page с именем News2016 в поле url
    context = {'page': page} # Передаем шаблон
    return render(request, 'siteapp/News2016.html', context) # Рендерим шаблон с передачей в него переменной page

def prod(request): # Для рендеринга страницы продукции
    page = Page.objects.get(url='Prod') # Получаем запись в таблице Page с именем Prod в поле url
    context = {'page': page} # Передаем шаблон
    return render(request, 'siteapp/Prod.html', context) # Рендерим шаблон с передачей в него переменной page

def grain(request): # Для рендеринга страницы зерновых
    page = Page.objects.get(url='Grain') # Получаем запись в таблице Page с именем Grain в поле url
    groups = CultureGroup.objects.get(name='Зерновые культуры') # Получаем запись в таблице Culture с нужным именем
    cultures = Culture.objects.filter(group=groups) # Получаем запись в таблице Culture с культурами этой группы
    taxons = Taxon.objects.filter(culture=cultures) # Получаем запись в таблице Taxon с таксонами этих культур
    context = {'page': page,'cultures': cultures, 'taxons': taxons} # Передаем записи в шаблон
    return render(request, 'siteapp/Grain.html', context) # Рендерим шаблон с передачей в него переменной page

def potato(request): # Для рендеринга страницы картофеля
    page = Page.objects.get(url='Potato') # Получаем запись в таблице Page с именем Potato в поле url
    groups = CultureGroup.objects.get(name='Клубнеплоды') # Получаем запись в таблице Culture с нужным именем
    cultures = Culture.objects.filter(group=groups) # Получаем запись в таблице Culture с культурами этой группы
    taxons = Taxon.objects.filter(culture=cultures) # Получаем запись в таблице Taxon с таксонами этих культур
    context = {'page': page, 'cultures': cultures, 'taxons': taxons} # Передаем записи в шаблон
    return render(request, 'siteapp/Potato.html', context) # Рендерим шаблон с передачей в него переменной page

def grass(request): # Для рендеринга страницы многолетних трав
    page = Page.objects.get(url='Grass') # Получаем запись в таблице Page с именем Grass в поле url
    groups = CultureGroup.objects.get(name='Многолетние травы') # Получаем запись в таблице Culture с нужным именем
    cultures = Culture.objects.filter(group=groups) # Получаем запись в таблице Culture с культурами этой группы
    taxons = Taxon.objects.filter(culture=cultures) # Получаем запись в таблице Taxon с таксонами этих культур
    context = {'page': page, 'cultures': cultures, 'taxons': taxons} # Передаем записи в шаблон
    return render(request, 'siteapp/Grass.html', context) # Рендерим шаблон с передачей в него переменной page

def jim(request): # Для рендеринга страницы жимолости
    page = Page.objects.get(url='Jim') # Получаем запись в таблице Page с именем Jim в поле url
    groups = CultureGroup.objects.get(name='Плодово-ягодные культуры') # Получаем запись в таблице Culture с нужным именем
    cultures = Culture.objects.filter(group=groups) # Получаем запись в таблице Culture с культурами этой группы
    taxons = Taxon.objects.filter(culture=cultures) # Получаем запись в таблице Taxon с таксонами этих культур
    context = {'page': page, 'cultures': cultures, 'taxons': taxons} # Передаем записи в шаблон
    return render(request, 'siteapp/Jim.html', context) # Рендерим шаблон с передачей в него переменной page

def about(request): # Для рендеринга страницы истории института
    page = Page.objects.get(url='About') # Получаем запись в таблице Page с именем About в поле url
    data = HistoryData.objects.all()  # Получаем все записи в таблице HistoryData
    histories = History.objects.all()  # Получаем все записи в таблице History
    context = {'page': page, 'histories': histories, 'data': data} # Передаем шаблон
    return render(request, 'siteapp/About.html', context) # Рендерим шаблон с передачей в него переменной page

def trend(request): # Для рендеринга страницы направлений деятельности
    page = Page.objects.get(url='Trend') # Получаем запись в таблице Page с именем Trend в поле url
    context = {'page': page} # Передаем шаблон
    return render(request, 'siteapp/Trend.html', context) # Рендерим шаблон с передачей в него переменной page

def progress(request): # Для рендеринга страницы достижений
    page = Page.objects.get(url='Progress') # Получаем запись в таблице Page с именем Progress в поле url
    progresses = Progress.objects.all()  # Получаем все записи в таблице Progress
    context = {'page': page, 'progresses': progresses} # Передаем в шаблон
    return render(request, 'siteapp/Progress.html', context) # Рендерим шаблон с передачей в него переменной page

def article(request): # Для рендеринга страницы статей
    page = Page.objects.get(url='Article') # Получаем запись в таблице Page с именем Article в поле url
    articles = Article.objects.all()  # Получаем все записи в таблице Article
    context = {'page': page, 'articles': articles} # Передаем шаблон
    return render(request, 'siteapp/Article.html', context) # Рендерим шаблон с передачей в него переменной page

def contact(request): # Для рендеринга страницы контактов
    page = Page.objects.get(url='Contact') # Получаем запись в таблице Page с именем Contact в поле url
    context = {'page': page} # Передаем шаблон
    return render(request, 'siteapp/Contact.html', context) # Рендерим шаблон с передачей в него переменной page

def price(request): # Для рендеринга страницы прайса
    page = Page.objects.get(url='Price') # Получаем запись в таблице Page с именем Price в поле url
    context = {'page': page} # Передаем шаблон
    return render(request, 'siteapp/Price.html', context) # Рендерим шаблон с передачей в него переменной page

def docs(request): # Для рендеринга страницы документов
    page = Page.objects.get(url='Docs') # Получаем запись в таблице Page с именем Docs в поле url
    context = {'page': page} # Передаем шаблон
    return render(request, 'siteapp/Docs.html', context) # Рендерим шаблон с передачей в него переменной page

def map(request): # Для рендеринга страницы карты сайта
    page = Page.objects.get(url='Map') # Получаем запись в таблице Page с именем Map в поле url
    context = {'page': page} # Передаем шаблон
    return render(request, 'siteapp/Map.html', context) # Рендерим шаблон с передачей в него переменной page

# Для отображения текущих и родительских страниц
def this_page(request, url):  # Для отображения текущей страницы
    context = {'page': {'url': url}} # Передаем в шаблон page переменную url
    return render(request, 'siteapp/index.html', context) #

def parent_page(request, parent_url): # Для отображения родительской страницы
    context = {'page': {'parent_url': parent_url}} # Передаем в шаблон page переменную parent_url
    return render(request, 'siteapp/index.html', context) # Рендерим шаблон с передачей в него переменной page