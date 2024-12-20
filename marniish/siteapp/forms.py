from django import forms # Для работы с формами
from .models import TrendBasic # Для работы с моделью

class ContactForm(forms.Form): # Форма для страницы с контактами для отправки сообщений в почту
    name = forms.CharField(label="Имя *", max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'Введите Ваше Имя'})) # Поле для ввода имени
    email = forms.EmailField(label="Электронная почта *", max_length=100,
                           widget=forms.EmailInput(attrs={'placeholder': 'email@email.ru'})) # Поле для ввода email
    subject = forms.CharField(label="Тема сообщения", max_length=150, required=False) # Поле для ввода темы
    message = forms.CharField(label="Сообщение *",
                              widget=forms.Textarea(attrs={'placeholder': 'Произвольный текст сообщения ...'})) # Поле для ввода сообщения

class TrendBasicAddForm(forms.ModelForm): # Форма для страницы с основными направлениями НИИ для добавления нового основного направления
    name = forms.CharField(label="Основное направление НИИ *", max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'Введите ещё одно основное направление НИИ'})) # Поле для ввода текста
    class Meta: # Класс для описания модели
        model = TrendBasic # Модель для описания основного направления НИИ
        fields = ['name'] # Основное направление (там и так только одно поле)