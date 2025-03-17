from django.contrib.auth.mixins import UserPassesTestMixin # Импортируем mixin для своего типа авторизации
from django.views.generic.base import ContextMixin  # Для создания общего класса миксинов
from .models import News, CultureGroup, Culture, Taxon, HistoryData, Document
import os # Здесь для удаления файлов из /media/

class AllYearsContextMixin(ContextMixin): # Миксин для добавления объектов в контекст
    def get_context_data(self, **kwargs): # Для передачи данных в контекст
        context = super().get_context_data(**kwargs) # Получаем базовый контекст
        context['all_years'] = News.objects.get_all_years() # Добавляем все годы в контекст, используя YearNewsManager
        return context # Передаём обновлённый контекст в страницу

class AdminRequiredMixin(UserPassesTestMixin): # Создаём миксин для разрешения доступа к странице только админу (хоть и лишь для одной)
    def test_func(self): # Для переопределения прав доступа
        return self.request.user.is_superuser # Только если пользователь админ (суперпользователь)

class CultureTaxonMixin(ContextMixin): # Миксин для добавления в контекст культуры и таксонов
    group_name = None # Определяем атрибут для имени группы
    def get_context_data(self, **kwargs): # Для передачи данных в контекст
        context = super().get_context_data(**kwargs) # Получаем базовый контекст
        context['group'] = CultureGroup.objects.get(name=self.group_name) # Добавляем запись таблицы CultureGroup с нужным именем в контекст
        context['cultures'] = Culture.objects.filter(group=context['group'])  # Добавляем запись таблицы Culture в контекст с культурами этой группы
        context['taxons'] = Taxon.objects.select_related('culture').filter(culture__in=context['cultures'])  # Добавляем запись таблицы Taxon в контекст с таксонами этих культур со связью с культурой
        return context # Передаём обновлённый контекст в страницу

class HistoriesDataMixin(ContextMixin): # Миксин для добавления в контекст всех данных истории
    def get_context_data(self, **kwargs): # Для передачи данных в контекст
        context = super().get_context_data(**kwargs) # Получаем базовый контекст
        context['data'] = HistoryData.objects.prefetch_related('history_set').all()  # Добавляем все записи таблицы HistoryData в контекст со связанными данными таблицы History
        return context # Передаём обновлённый контекст в страницу

class DocsMixin(ContextMixin): # Миксин для добавления def get_context_data и def form_valid
    def get_context_data(self, **kwargs): # Для передачи данных в контекст
        context = super().get_context_data(**kwargs) # Получаем базовый контекст
        context['docs'] = Document.objects.all() # Добавляем все записи таблицы Document в контекст
        return context # Передаём обновлённый контекст в страницу
    def form_valid(self, form): # Для переопределения работы с правильными данными
        one_doc = self.get_object() # Получаем текущий объект
        if one_doc.url and os.path.isfile(one_doc.url.path): # Если есть медиафайл с соответствующим url
            os.remove(one_doc.url.path) # то удаляем старый файл перед сохранением нового
        return super().form_valid(form) # Вызываем стандартный метод form_valid