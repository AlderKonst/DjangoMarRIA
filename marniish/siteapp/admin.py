from django.contrib import admin
from .models import * # Все имеющиеся модели загружаем

admin.site.register(Trend) # Регистрируем модель с основными направлениями
admin.site.register(Article) # Регистрируем модель со статьями
admin.site.register(Progress) # Регистрируем модель с достижениями
admin.site.register(Page) # Регистрируем модель для шаблонов страниц
admin.site.register(TrendItem) # Регистрируем модель с пунктами направлений деятельности
admin.site.register(Reference) # Регистрируем модель с полезными ссылками
admin.site.register(HistoryData) # Регистрируем модель с историческими датами
admin.site.register(History) # Регистрируем модель с историческими событиями к датам
admin.site.register(CultureGroup) # Регистрируем модель с группами культур
admin.site.register(Culture) # Регистрируем модель с видами, воздеваемых в НИИ культур
class TaxonAdmin(admin.ModelAdmin): # Для расширения возможностей админки
    list_display = ['name', 'culture'] # Поля в виде колонок с возможностью сортировки
admin.site.register(Taxon, TaxonAdmin) # Регистрируем модель с таксонами, воздеваемых в НИИ культур
class DocumentAdmin(admin.ModelAdmin): # Для расширения возможностей админки
    list_display = ['date', 'name', 'url'] # Поля в виде колонок с возможностью сортировки
admin.site.register(Document, DocumentAdmin) # Регистрируем модель с публикованными документами НИИ
admin.site.register(ProdCategory) # Регистрируем модель с названиями категорий продукции
class PriceAdmin(admin.ModelAdmin): # Для расширения возможностей админки
    list_display = ['taxon__culture', 'taxon', 'category', 'mass', 'price'] # Поля в виде колонок с возможностью сортировки
admin.site.register(Price, PriceAdmin) # Регистрируем модель с ценами
admin.site.register(NewsPicture) # Регистрируем модель с картинками для новостей
admin.site.register(News) # Регистрируем модель с событием НИИ

