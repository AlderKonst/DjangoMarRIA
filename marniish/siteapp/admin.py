from django.contrib import admin
from .models import * # Все модели загружаем (Trend, Article, Progress, Page, TrendItem, Reference)

admin.site.register(Trend) # Регистрируем модель Trend
admin.site.register(Article) # Регистрируем модель Article
admin.site.register(Progress) # Регистрируем модель Progress
admin.site.register(Page) # Регистрируем модель Page
admin.site.register(TrendItem) # Регистрируем модель TrendItem
admin.site.register(Reference) # Регистрируем модель Reference