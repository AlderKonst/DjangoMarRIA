from django import forms # Для работы с формами
from django.db.models import Max # Для получения максимального значения в БД
from .models import TrendItem, Trend, Document, History, Article, Progress # Для работы с моделью

class ArticleEditingForm(forms.ModelForm): # Форма для страницы со списком статей НИИ
    year = forms.IntegerField( # Поле для ввода года публикации статьи
        label="Год *", # Метка для поля ввода года
        widget=forms.TextInput( # Виджет для ввода текста в html-код
            attrs={'placeholder': 'Введите год'})) # Подсказка для ввода года
    trend = forms.ModelChoiceField( # Поле выбора основного направления
        label="Основное направление НИИ *", # Метка для поля выбора основного направления НИИ
        queryset=Trend.objects.all(), # Получение всех объектов модели Trend
        widget=forms.Select())  # Использование стандартного виджета выбора
    name = forms.CharField( # Поле для ввода статьи
        label="Статья *", # Метка для поля ввода статьи
        max_length=500, # Максимальное количество символов статьи
        widget=forms.TextInput( # Виджет для ввода текста в html-код
            attrs={'placeholder': 'Введите статью'})) # Подсказка для ввода статьи
    doi = forms.CharField( # Поле для ввода DOI документа
        label="DOI", # Метка для поля ввода DOI документа
        max_length=50, # Максимальное количество символов DOI
        required=False, # Поле не является обязательным для заполнения
        widget=forms.TextInput( # Виджет для ввода текста в html-код
            attrs={'placeholder': 'Введите без https://doi.org/'})) # Подсказка для ввода DOI документа
    link = forms.CharField( # Поле для ввода ссылки
        label="URL", # Метка для поля ввода ссылки
        max_length=100, # Максимальное количество символов ссылки
        required=False, # Поле не является обязательным для заполнения
        widget=forms.TextInput( # Виджет для ввода текста в html-код
             attrs={'placeholder': 'Введите полный URL'})) # Подсказка для ввода ссылки
    def __init__(self, *args, **kwargs): # Конструктор формы
        super().__init__(*args, **kwargs) # Вызываем метод родительского класса
        max_year = Article.objects.aggregate(Max('year'))['year__max'] # Получаем максимальный год из БД (спасибо нейросети)
        self.fields['year'].initial = max_year # Устанавливаем значение по умолчанию для поля year
        self.fields['trend'].initial = Trend.objects.get(name='plant') # Устанавливаем значение по умолчанию для поля trend
    class Meta: # Класс для работы с моделью формы
        model = Article # Модель для работы с моделью
        fields = ['year', 'trend', 'name', 'doi', 'link'] # Поля для работы с моделью

class ProgressEditingForm(forms.ModelForm): # Форма для страницы со списком достижений НИИ
    year = forms.IntegerField( # Поле для ввода года достижения
        label="Год *", # Метка для поля ввода года
        widget=forms.TextInput( # Виджет для ввода текста в html-код
            attrs={'placeholder': 'Введите год'})) # Подсказка для ввода года
    trend = forms.ModelChoiceField( # Поле выбора основного направления
        label="Основное направление НИИ *", # Метка для поля выбора основного направления НИИ
        queryset=Trend.objects.all(), # Получение всех объектов модели Trend
        widget=forms.Select()) # Использование стандартного виджета выбора
    name = forms.CharField( # Поле для ввода достижения
        label="Достижение *", # Метка для поля ввода достижения
        max_length=250, # Максимальное количество символов достижения
        widget=forms.TextInput( # Виджет для ввода текста в html-код
            attrs={'placeholder': 'Введите достижение'})) # Подсказка для ввода достижения
    def __init__(self, *args, **kwargs): # Конструктор формы
        super().__init__(*args, **kwargs) # Вызываем метод родительского класса
        max_year = Article.objects.aggregate(Max('year'))['year__max'] # Получаем максимальный год из БД (спасибо нейросети)
        self.fields['year'].initial = max_year # Устанавливаем значение по умолчанию для поля year
        self.fields['trend'].initial = Trend.objects.get(name='plant') # Устанавливаем значение по умолчанию для поля trend
    class Meta: # Класс для работы с моделью
        model = Progress # Модель для работы с моделью
        fields = ['year', 'trend', 'name'] # Поля для работы с моделью

class HistoryEditingForm(forms.ModelForm): # Форма для страницы с событием НИИ
    year = forms.IntegerField( # Поле для ввода года
        label="Год *", # Метка для поля ввода года
        widget=forms.TextInput( # Виджет для ввода текста в html-код
            attrs={'placeholder': 'Введите год'})) # Подсказка для ввода года
    day_month = forms.CharField( # Поле для ввода дня и месяца
        label="День и месяц", # Метка для поля ввода дня и месяца
        max_length=15, # Максимальная количество символов текста строки
        required=False, # Поле не является обязательным
        widget=forms.TextInput( # Виджет для ввода текста в html-код
            attrs={'placeholder': '22 февраля (образец)'})) # Подсказка для ввода дня и месяца
    text = forms.CharField( # Поле для ввода текста абзаца
        label="Текст абзаца *", # Метка для поля ввода текста абзаца
        max_length=1500, # Максимальная количество символов текста абзаца
        widget=forms.Textarea( # Виджет для ввода большого текста в html-код
            attrs={'placeholder': 'Текст абзаца ...'})) # Подсказка для ввода текста абзаца
    img = forms.CharField( # Поле для ввода URL изображения
        label="URL изображения", # Метка для поля ввода URL изображения
        required=False, # Поле не является обязательным
        widget=forms.TextInput( # Виджет для ввода текста в html-код
            attrs={'placeholder': 'Сперва скопировать в папку static!'}))  # Подсказка по загрузке изображения
    alt = forms.CharField( # Поле для ввода описания картинки
        label="Описание картинки", # Метка для поля ввода описания картинки
        max_length=100, # Максимальная количество символов текста описания картинки
        required=False, # Поле не является обязательным
        widget=forms.TextInput( # Виджет для ввода текста в html-код
            attrs={'placeholder': 'Описание'})) # Подсказка для ввода описания картинки
    class Meta: # Класс для описания модели
        model = History # Модель для описания события
        fields = ['year', 'day_month', 'text', 'img', 'alt'] # Дата события, текст абзаца, фото и его описание

class ContactForm(forms.Form): # Форма для страницы с контактами для отправки сообщений в почту
    name = forms.CharField( # Поле для ввода имени
        label="Имя *", # Метка для поля ввода имени
        max_length=100, # Максимальная количество символов текста имени
        widget=forms.TextInput( # Виджет для ввода текста в html-код
            attrs={'placeholder': 'Введите Ваше Имя'})) # Подсказка для ввода имени
    email = forms.EmailField( # Поле для ввода email адреса
        label="Электронная почта *", # Метка для поля ввода email
        max_length=100, # Максимальная количество символов email адреса
        widget=forms.EmailInput( # Виджет для ввода емейла в html-код
            attrs={'placeholder': 'email@email.ru'})) # Подсказка для ввода email адреса
    subject = forms.CharField( # Поле для ввода темы сообщения
        label="Тема сообщения", # Метка для поля ввода темы сообщения
        max_length=150, # Максимальная количество символов текста темы сообщения
        required=False, # Поле не является обязательным
        widget=forms.TextInput( # Виджет для ввода текста в html-код
            attrs={'placeholder': 'Введите Тему сообщения'})) # Подсказка для ввода темы сообщения
    message = forms.CharField( # Поле для ввода сообщения
        label="Сообщение *", # Метка для поля ввода сообщения
        widget=forms.Textarea( # Виджет для ввода большого текста в html-код
            attrs={'placeholder': 'Произвольный текст сообщения ...'})) # Подсказка для ввода текста сообщения

class TrendItemAddForm(forms.ModelForm): # Форма для страницы с направлениями НИИ для добавления нового направления
    name = forms.CharField( # Поле для ввода текста направления
        label="Направление деятельности НИИ *", # Метка для поля ввода направления деятельности НИИ
        max_length=250, # Максимальная количество символов текста названия направления
        widget=forms.TextInput( # Виджет для ввода текста в html-код
            attrs={'placeholder': 'Введите ещё одно направление деятельности НИИ'})) # Подсказка для ввода направления
    trend = forms.ModelChoiceField( # Поле выбора основного направления
        label="Основное направление НИИ *", # Метка для поля выбора основного направления НИИ
        queryset=Trend.objects.all(), # Получение всех объектов модели Trend
        widget=forms.Select()) # Использование стандартного виджета выбора
    class Meta: # Класс для описания модели
        model = TrendItem # Модель для описания пункта основного направления НИИ
        fields = ['name', 'trend'] # Пункт основного направления и основное направление деятельности НИИ

class DocsAddForm(forms.ModelForm): # Форма для добавления документов в систему
    date = forms.DateField( # Поле для выбора даты публикации документа
        widget=forms.DateInput( # Виджет для ввода даты в html-код
            attrs={'type': 'date'}), # Указываем тип поля как дата
            label="Дата публикации документа") # Указываем метку здесь
    name = forms.CharField( # Поле для ввода названия документа
        label="Название документа", # Метка для поля ввода названия документа
        max_length=250, # Максимальная количество символов текста названия документа
        widget=forms.Textarea( # Виджет для ввода большого текста в html-код
            attrs={'placeholder': 'Введите название документа'})) # Подсказка для ввода названия документа
    url = forms.FileField( # Поле для загрузки документа
        label="Загрузить документ", # Метка для загрузки документа, с загрузкой в /media/
        widget=forms.FileInput( # Виджет для загрузки документа через html-код
            attrs={'accept': '.pdf,.doc,.docx'})) # Такие форматы лишь будут допустимы
    class Meta: # Класс для описания модели
        model = Document # Модель для описания документов
        fields = ['date', 'url', 'name'] # Дата публикации документа, его название и URL

