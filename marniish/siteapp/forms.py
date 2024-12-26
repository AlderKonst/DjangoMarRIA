from django import forms # Для работы с формами
from .models import TrendItem, Trend, Document, HistoryData, History  # Для работы с моделью

class HistoryDataAddForm(forms.ModelForm): # Форма для страницы с датами событий НИИ
    year = forms.IntegerField(label="Год *",
                              widget=forms.TextInput(attrs={'placeholder': 'Введите год'})) # Поле для ввода года
    day_month = forms.CharField(label="День и месяц", max_length=15, required=False,
                                widget=forms.TextInput(attrs={'placeholder': '22 февраля (образец)'})) # Поле для ввода дня и месяца
    class Meta: # Класс для описания модели
        model = HistoryData # Модель для описания даты события
        fields = ['year', 'day_month'] # Год и день с месяцем события

class HistoryAddForm(forms.ModelForm): # Форма для страницы с абзацем события НИИ
    data = forms.ModelChoiceField( # Создание поля выбора даты
        label="Дата события *", # Метка для поля выбора
        queryset=HistoryData.objects.all(), # Получение всех объектов модели HistoryData
        widget=forms.Select()) # Использование стандартного виджета выбора
    text = forms.CharField(label="Текст абзаца *", max_length=1500,
                           widget=forms.Textarea(attrs={'placeholder': 'Текст обзаца ...'})) # Поле для ввода текста абзаца
    img = forms.CharField(label="URL изображения", required=False, # URL изображения в /static/ (крайне редко меняется)
                          widget=forms.TextInput(attrs={'placeholder': 'Сперва скопировать в папку static!'})) # Такие форматы лишь будут допустимы
    alt = forms.CharField(label="Описание картинки", max_length=100, required=False,
                          widget=forms.TextInput(attrs={'placeholder': 'Описание'}))  # Поле для ввода описания картинки
    class Meta: # Класс для описания модели
        model = History # Модель для абзаца события
        fields = ['data', 'text', 'img', 'alt'] # Дата события, текст абзаца, фото и его описание

class ContactForm(forms.Form): # Форма для страницы с контактами для отправки сообщений в почту
    name = forms.CharField(label="Имя *", max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'Введите Ваше Имя'})) # Поле для ввода имени
    email = forms.EmailField(label="Электронная почта *", max_length=100,
                             widget=forms.EmailInput(attrs={'placeholder': 'email@email.ru'})) # Поле для ввода email
    subject = forms.CharField(label="Тема сообщения", max_length=150, required=False,
                              widget=forms.TextInput(attrs={'placeholder': 'Введите Тему сообщения'})) # Поле для ввода темы
    message = forms.CharField(label="Сообщение *",
                              widget=forms.Textarea(attrs={'placeholder': 'Произвольный текст сообщения ...'})) # Поле для ввода сообщения

class TrendItemAddForm(forms.ModelForm): # Форма для страницы с направлениями НИИ для добавления нового направления
    name = forms.CharField(label="Направление деятельности НИИ *", max_length=250,
                           widget=forms.TextInput(attrs={'placeholder': 'Введите ещё одно направление деятельности НИИ'})) # Поле для ввода текста
    trend = forms.ModelChoiceField( # Создание поля выбора основного направления
        label="Основное направление НИИ *", # Метка для поля выбора
        queryset=Trend.objects.all(), # Получение всех объектов модели Trend
        widget=forms.Select()) # Использование стандартного виджета выбора
    class Meta: # Класс для описания модели
        model = TrendItem # Модель для описания пункта основного направления НИИ
        fields = ['name', 'trend'] # Пункт основного направления и основное направление деятельности НИИ

class DocsAddForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), # Указываем тип для html
        label="Дата публикации документа") # Указываем label здесь почему-то
    name = forms.CharField(label="Название документа", max_length=250,
                           widget=forms.Textarea(attrs={'placeholder': 'Введите название документа'}))
    url = forms.FileField(label="Загрузить документ", # URL документа, с загрузкой в /media/
                          widget=forms.FileInput(attrs={'accept': '.pdf,.doc,.docx'})) # Такие форматы лишь будут допустимы
    class Meta: # Класс для описания модели
        model = Document # Модель для описания документов
        fields = ['date', 'url', 'name'] # Дата публикации документа, его название и URL