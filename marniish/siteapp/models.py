from django.db import models

class Trend(models.Model):# Основные направления деятельности института
    name = models.CharField(max_length=10, unique=True) # Название направления (достаточно было и 5)
    def __str__(self):
        return self.name # Возвращает название направления

class Article(models.Model): # Статьи
    name = models.CharField(max_length=500, unique=True)  # Библиоинфа из не более 500 символов (обычно их до 300)
    year = models.IntegerField() # Год
    trend = models.ForeignKey(Trend, on_delete=models.CASCADE) # Направление деятельности
    doi = models.CharField(max_length=50, blank=True)  # Значение DOI не выше 50 символов (обычно их до 40)
    link = models.CharField(max_length=100, blank=True)  # Ссылка на статью
    def __str__(self):
        return self.name # Возвращает библиоинфу

class Progress(models.Model): # Наиболее значимые достижения по направлениям НИР
    name = models.CharField(max_length=250) # Название достижения
    year = models.IntegerField() # Год
    trend = models.ForeignKey(Trend, on_delete=models.CASCADE)  # Направление деятельности
    def __str__(self):
        return self.name # Возвращает наименование достижения

class PageWay(models.Model): # Путь и имя страницы
    url = models.URLField(max_length=30, unique=True)  # URL страницы (без .html)
    title = models.CharField(max_length=50)  # Название страницы

class Page(models.Model): # Содержимое сайта
    page = models.ForeignKey(PageWay, on_delete=models.CASCADE) # ID пути страницы
    description = models.CharField(max_length=100) # Метаописание страницы
    parent = models.ForeignKey('self', # Самоссылка для указания родительской страницы
                               null=True, blank=True, on_delete=models.CASCADE)
