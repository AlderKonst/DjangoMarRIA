from django.shortcuts import (render, # Импортируем функцию для рендеринга шаблонов,
                              get_object_or_404, # получения объекта или возврата 404 ошибки
                              HttpResponseRedirect) # и перенаправления
from django.urls import reverse, reverse_lazy # Импортируем функцию для получения URL по имени
from django.core.mail import EmailMessage # Импортируем функцию для отправки электронной почты
from django.utils.encoding import force_bytes # Импортируем функцию для кодирования
from .models import (Page, TrendItem, Reference, Article, Progress, History,
                     HistoryData, Culture, Taxon, CultureGroup, Document, Price, News)  # Импортируем модели соответствующих таблиц
from .forms import ContactForm, TrendItemAddForm, DocsAddForm # Импортируем формы
import os # Здесь для удаления файла из /media/

from django.views.generic.base import ContextMixin # Для создания общего класса
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView # Базовые классы

class PageContextMixin(ContextMixin): # Миксин для добавления объекта Page в контекст
    page_url = None # Инициируем переменную
    def get_context_data(self, **kwargs): # Для передачи данных в контекст
        context = super().get_context_data(**kwargs) # Получаем базовый контекст
        context['page'] = get_object_or_404(Page, url=self.page_url) # Добавляем страницу в контекст
        return context # Возвращаем контекст

class IndexTemplateView(PageContextMixin, TemplateView): # Для рендеринга главной страницы
    page_url = 'index' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    template_name = 'siteapp/index.html' # Указываем расположение шаблона рендеринга
    def get_context_data(self, **kwargs): # Для передачи данных в контекст
        context = super().get_context_data(**kwargs) # Получаем базовый контекст
        context['trends'] = TrendItem.objects.all() # Добавляем все записи таблицы TrendItem в контекст
        context['references'] = Reference.objects.all() # Добавляем все записи таблицы Reference в контекст
        return context # Передаём обновлённый контекст в страницу

class NewsListView(PageContextMixin, ListView): # Для рендеринга страницы новостей
    template_name = 'siteapp/News.html' # Указываем расположение шаблона рендеринга
    context_object_name = 'newses' # Указываем имя контекста
    def get_queryset(self): # Для получения записей в таблице News
        self.year = self.kwargs['year'] # Получаем значение поля year (благодаря self. ненужно передавать в контексте с помощью def get_context_data)
        self.page_url = self.year # Создаём наследованный из ContextMixin контекст из записи таблицы Page
        return News.objects.filter(date__year=self.year # Получаем записи этого (year) года в таблице News со
                                   ).prefetch_related('news_blocks') # связанными блоками NewsBlock, через имя 'news_bloks'
    def get_context_data(self, **kwargs): # Для передачи данных в контекст
        context = super().get_context_data(**kwargs) # Получаем базовый контекст
        context['year'] = self.year # Добавляем year в контекст (столько кода из-за одного year!!!)
        return context # Передаём обновлённый контекст в страницу

class ContactTemplateView(PageContextMixin, TemplateView): # Для рендеринга страницы контактов (вот тебе и, блин, сокращённый код)
    page_url = 'Contact' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    template_name = 'siteapp/Contact.html' # Указываем расположение шаблона рендеринга
    success_url = reverse_lazy('siteapp:Contact') # Перенаправляем на страницу контактов даже при успешном отправлении сообщения
    def get_context_data(self, **kwargs): # Для передачи данных в контекст
        context = super().get_context_data(**kwargs) # Получаем базовый контекст
        context['form'] = ContactForm() # Добавляем форму в контекст
        return context # Передаём обновлённый контекст в страницу
    def post(self, request): # Для обработки данных формы
        form = ContactForm(request.POST) # Загружаем данные, полученные из формы
        if form.is_valid(): # Если форма валидна (все данные правильные)
            name = form.cleaned_data['name'] # Имя отправившего сообщение
            email = form.cleaned_data['email'] # Email отправившего сообщение
            subject = form.cleaned_data['subject'] or "Сообщение с сайта" # Тема отправившего сообщение с возможным значением по умолчанию
            message = form.cleaned_data['message'] # Сообщение отправившего сообщение
            message_txt = f"{message}\nОт: {name} <{email}>" # Текст сообщения
            email_message = EmailMessage( # Тут оказывается есть более новое и универсальное решение, чем send_email()
                subject, # Тема сообщения, на русском не работает правильно
                f'Тема сообщения: {subject}\nТекст сообщения: {message_txt}\n', # Тема и текст сообщения
                email, # Email отправившего сообщение
                ['marniish@yandex.ru']) # Кому отправляем
            email_message.send(fail_silently=False) # Отправляем сообщение
            return HttpResponseRedirect(self.success_url) # Перенаправляем на главную страницу
        else: # Если данные формы неправильные
            context = self.get_context_data() # Создаем контекст
            context['form'] = form # Добавляем форму в контекст
            return render(request, self.template_name, context) # Рендерим шаблон с передачей в него контекста

class ProdTemplateView(PageContextMixin, TemplateView): # Для рендеринга главной страницы
    page_url = 'Prod' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    template_name = 'siteapp/Prod.html' # Указываем расположение шаблона рендеринга

class GrainTemplateView(PageContextMixin, TemplateView): # Для рендеринга страницы зерновых
    page_url = 'Grain' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    template_name = 'siteapp/Grain.html' # Указываем расположение шаблона рендеринга
    def get_context_data(self, **kwargs): # Для передачи данных в контекст
        context = super().get_context_data(**kwargs) # Получаем базовый контекст
        context['group'] = CultureGroup.objects.get(name='Зерновые культуры') # Добавляем запись таблицы CultureGroup с нужным именем в контекст
        context['cultures'] = Culture.objects.filter(group=context['group']) # Добавляем запись таблицы Culture в контекст с культурами этой группы
        context['taxons'] = Taxon.objects.filter(culture__in=context['cultures']) # Добавляем запись таблицы Taxon в контекст с таксонами этих культур
        return context # Передаём обновлённый контекст в страницу

class PotatoTemplateView(PageContextMixin, TemplateView): # Для рендеринга страницы клубнеплодов
    page_url = 'Potato' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    template_name = 'siteapp/Potato.html' # Указываем расположение шаблона рендеринга
    def get_context_data(self, **kwargs): # Для передачи данных в контекст
        context = super().get_context_data(**kwargs) # Получаем базовый контекст
        context['group'] = CultureGroup.objects.get(name='Клубнеплоды') # Добавляем запись таблицы CultureGroup с нужным именем в контекст
        context['cultures'] = Culture.objects.filter(group=context['group']) # Добавляем запись таблицы Culture в контекст с культурами этой группы
        context['taxons'] = Taxon.objects.filter(culture__in=context['cultures']) # Добавляем запись таблицы Taxon в контекст с таксонами этих культур
        return context # Передаём обновлённый контекст в страницу

class GrassTemplateView(PageContextMixin, TemplateView): # Для рендеринга страницы многолетних трав
    page_url = 'Grass' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    template_name = 'siteapp/Grass.html' # Указываем расположение шаблона рендеринга
    def get_context_data(self, **kwargs): # Для передачи данных в контекст
        context = super().get_context_data(**kwargs) # Получаем базовый контекст
        context['group'] = CultureGroup.objects.get(name='Многолетние травы') # Добавляем запись таблицы CultureGroup с нужным именем в контекст
        context['cultures'] = Culture.objects.filter(group=context['group']) # Добавляем запись таблицы Culture в контекст с культурами этой группы
        context['taxons'] = Taxon.objects.filter(culture__in=context['cultures']) # Добавляем запись таблицы Taxon в контекст с таксонами этих культур
        return context # Передаём обновлённый контекст в страницу

class JimTemplateView(PageContextMixin, TemplateView): # Для рендеринга страницы жимолости
    page_url = 'Jim' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    template_name = 'siteapp/Jim.html' # Указываем расположение шаблона рендеринга
    def get_context_data(self, **kwargs): # Для передачи данных в контекст
        context = super().get_context_data(**kwargs) # Получаем базовый контекст
        context['group'] = CultureGroup.objects.get(name='Плодово-ягодные культуры') # Добавляем запись таблицы CultureGroup с нужным именем в контекст
        context['cultures'] = Culture.objects.filter(group=context['group']) # Добавляем запись таблицы Culture в контекст с культурами этой группы
        context['taxons'] = Taxon.objects.filter(culture__in=context['cultures']) # Добавляем запись таблицы Taxon в контекст с таксонами этих культур
        return context # Передаём обновлённый контекст в страницу

class AboutTemplateView(PageContextMixin, TemplateView): # Для рендеринга страницы истории института
    page_url = 'About' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    template_name = 'siteapp/About.html' # Указываем расположение шаблона рендеринга
    def get_context_data(self, **kwargs): # Для передачи данных в контекст
        context = super().get_context_data(**kwargs) # Получаем базовый контекст
        context['histories'] = History.objects.all() # Добавляем все записи таблицы History в контекст
        context['data'] = HistoryData.objects.all() # Добавляем все записи таблицы HistoryData в контекст
        return context # Передаём обновлённый контекст в страницу

class TrendListView(PageContextMixin, ListView): # Для рендеринга страницы направлений деятельности
    page_url = 'Trend' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    template_name = 'siteapp/Trend.html' # Указываем расположение шаблона рендеринга
    queryset = TrendItem.objects.all() # Добавляем все записи таблицы TrendItem в контекст
    context_object_name = 'lis' # Указываем имя переменной контекста таким

class TrendEditingView(PageContextMixin, CreateView, ListView): # Для рендеринга страницы редактирования направлений деятельности
    page_url = 'Trend_editing' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    model = TrendItem # Указываем модель
    form_class = TrendItemAddForm # Указываем форму с передачей в виде контекста как 'form'
    template_name = 'siteapp/Trend_editing.html' # Указываем расположение шаблона рендеринга
    success_url = reverse_lazy('siteapp:Trend_editing') # Перенаправляем на страницу редактирования даже при успешном отправлении сообщения
    context_object_name = 'lis' # Указываем имя переменной контекста таким

class TrendEditUpdateView(PageContextMixin, UpdateView): # Для рендеринга страницы редактирования направлений деятельности
    page_url = 'Trend_edit' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    model = TrendItem # Указываем модель
    form_class = TrendItemAddForm # Указываем форму с передачей в виде контекста как 'form'
    template_name = 'siteapp/Trend_edit.html' # Указываем расположение шаблона рендеринга
    success_url = reverse_lazy('siteapp:Trend_editing') # Перенаправляем на страницу редактирования при успешном отправлении сообщения
    def get_context_data(self, **kwargs): # Для передачи данных в контекст
        context = super().get_context_data(**kwargs) # Получаем базовый контекст
        context['lis'] = TrendItem.objects.all()  # Добавляем все записи таблицы TrendItem в контекст
        return context # Передаём обновлённый контекст в страницу

class TrendDeleteView(PageContextMixin, DeleteView): # Для рендеринга страницы редактирования направлений деятельности
    page_url = 'Trend_confirm_delete' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    model = TrendItem # Указываем модель
    template_name = 'siteapp/Trend_confirm_delete.html' # Указываем расположение шаблона рендеринга
    success_url = reverse_lazy('siteapp:Trend_editing') # Перенаправляем на страницу редактирования при успешном отправлении сообщения
    context_object_name = 'trend' # Указываем имя переменной контекста таким
    def get_context_data(self, **kwargs): # Для передачи данных в контекст
        context = super().get_context_data(**kwargs) # Получаем базовый контекст
        context['lis'] = TrendItem.objects.all() # Добавляем все записи таблицы TrendItem в контекст
        return context # Передаём обновлённый контекст в страницу

class ProgressListView(PageContextMixin, ListView): # Для рендеринга страницы направлений деятельности
    page_url = 'Progress' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    template_name = 'siteapp/Progress.html' # Указываем расположение шаблона рендеринга
    context_object_name = 'progresses' # Указываем имя переменной контекста таким
    queryset = Progress.objects.all() # Добавляем все записи таблицы TrendItem в контекст

class ArticleListView(PageContextMixin, ListView): # Для рендеринга страницы статей
    page_url = 'Article' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    template_name = 'siteapp/Article.html' # Указываем расположение шаблона рендеринга
    context_object_name = 'articles' # Указываем имя переменной контекста таким
    queryset = Article.objects.all() # Добавляем все записи таблицы Article в контекст

class PriceListView(PageContextMixin, ListView): # Для рендеринга страницы прайс-листа
    page_url = 'Price' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    template_name = 'siteapp/Price.html' # Указываем расположение шаблона рендеринга
    context_object_name = 'prices' # Указываем имя переменной контекста таким
    queryset = Price.objects.all() # Добавляем все записи таблицы Price в контекст

class DocsListView(PageContextMixin, ListView): # Для рендеринга страницы документов
    page_url = 'Docs' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    template_name = 'siteapp/Docs.html' # Указываем расположение шаблона рендеринга
    context_object_name = 'docs' # Указываем имя переменной контекста таким
    queryset = Document.objects.all() # Добавляем все записи таблицы Document в контекст

class DocsEditingView(PageContextMixin, CreateView, ListView): # Для рендеринга страницы редактирования направлений деятельности
    page_url = 'Docs_editing' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    model = Document # Указываем модель
    form_class = DocsAddForm # Указываем форму с передачей в виде контекста как 'form'
    template_name = 'siteapp/Docs_editing.html' # Указываем расположение шаблона рендеринга
    success_url = reverse_lazy('siteapp:Docs_editing') # Перенаправляем на страницу редактирования даже при успешном отправлении сообщения
    context_object_name = 'docs' # Указываем имя переменной контекста таким

class DocsEditUpdateView(PageContextMixin, UpdateView): # Для рендеринга страницы редактирования направлений деятельности
    page_url = 'Docs_edit' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    model = Document # Указываем модель
    form_class = DocsAddForm # Указываем форму с передачей в виде контекста как 'form'
    template_name = 'siteapp/Docs_edit.html' # Указываем расположение шаблона рендеринга
    success_url = reverse_lazy('siteapp:Docs_editing') # Перенаправляем на страницу редактирования при успешном отправлении сообщения
    def get_context_data(self, **kwargs): # Для передачи данных в контекст
        context = super().get_context_data(**kwargs) # Получаем базовый контекст
        context['docs'] = Document.objects.all() # Добавляем все записи таблицы Document в контекст
        return context # Передаём обновлённый контекст в страницу
    def form_valid(self, form): # Для переопределения работы с правильными данными
        one_doc = self.get_object() # Получаем текущий объект
        if one_doc.url and os.path.isfile(one_doc.url.path): # Если есть медиафайл с соответствующим url
            os.remove(one_doc.url.path) # то удаляем старый файл перед сохранением нового
        return super().form_valid(form) # Вызываем стандартный метод form_valid

class DocsDeleteView(PageContextMixin, DeleteView): # Для рендеринга страницы редактирования направлений деятельности
    page_url = 'Docs_confirm_delete' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    model = Document # Указываем модель
    template_name = 'siteapp/Docs_confirm_delete.html' # Указываем расположение шаблона рендеринга
    success_url = reverse_lazy('siteapp:Docs_editing') # Перенаправляем на страницу редактирования при успешном отправлении сообщения
    context_object_name = 'one_doc' # Указываем имя переменной контекста таким
    def get_context_data(self, **kwargs): # Для передачи данных в контекст
        context = super().get_context_data(**kwargs) # Получаем базовый контекст
        context['docs'] = Document.objects.all() # Добавляем все записи таблицы Document в контекст
        return context # Передаём обновлённый контекст в страницу
    def form_valid(self, form): # Для переопределения работы с правильными данными
        one_doc = self.get_object() # Получаем текущий объект
        if one_doc.url and os.path.isfile(one_doc.url.path): # Если есть медиафайл с соответствующим url
            os.remove(one_doc.url.path) # то удаляем старый файл перед сохранением нового
        return super().form_valid(form) # Вызываем стандартный метод form_valid

class MapTemplateView(PageContextMixin, TemplateView): # Для рендеринга страницы карты сайта
    page_url = 'Map' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    template_name = 'siteapp/Map.html' # Указываем расположение шаблона рендеринга

class PageTemplateView(TemplateView): # Для отображения путей к страницам
    template_name = 'siteapp/index.html' # Указываем расположение шаблона рендеринга
    def get_context_data(self, **kwargs): # Для передачи данных в контекст
        context = super().get_context_data(**kwargs) # Получаем базовый контекст
        context['page'] = Page.objects.get(url=kwargs['url']) # Добавляем url в цикл контекста
        return context # Передаём обновлённый контекст в страницу