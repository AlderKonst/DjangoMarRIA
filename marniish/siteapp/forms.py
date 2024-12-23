from django import forms # Для работы с формами
from .models import TrendItem, Trend # Для работы с моделью

class ContactForm(forms.Form): # Форма для страницы с контактами для отправки сообщений в почту
    name = forms.CharField(label="Имя *", max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'Введите Ваше Имя'})) # Поле для ввода имени
    email = forms.EmailField(label="Электронная почта *", max_length=100,
                           widget=forms.EmailInput(attrs={'placeholder': 'email@email.ru'})) # Поле для ввода email
    subject = forms.CharField(label="Тема сообщения", max_length=150, required=False) # Поле для ввода темы
    message = forms.CharField(label="Сообщение *",
                              widget=forms.Textarea(attrs={'placeholder': 'Произвольный текст сообщения ...'})) # Поле для ввода сообщения

class TrendItemAddForm(forms.ModelForm): # Форма для страницы с направлениями НИИ для добавления нового направления
    name = forms.CharField(label="Направление деятельности НИИ *", max_length=250,
                           widget=forms.TextInput(attrs={'placeholder': 'Введите ещё одно направление деятельности НИИ'})) # Поле для ввода текста
    trend = forms.ModelChoiceField( # Создание поля выбора модели
        label="Основное направление НИИ *", # Метка для поля выбора
        queryset=Trend.objects.all(), # Получение всех объектов модели Trend
        widget=forms.Select()) # Использование стандартного виджета выбора
    class Meta: # Класс для описания модели
        model = TrendItem # Модель для описания пункта основного направления НИИ
        fields = ['name', 'trend'] # Пункт основного направления и основное направление деятельности НИИ