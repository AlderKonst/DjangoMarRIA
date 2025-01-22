from siteapp.views import PageContextMixin # Импортируем миксин из siteapp
from django.contrib.auth.views import LoginView # Импортируем класс для авторизации
from .forms import RegistrationForm # Импортируем форму регистрации
from django.views.generic import CreateView # Импортируем базовый класс для создания
from .models import SiteUser # Импортируем модель пользователя SiteUser
from django.urls import reverse_lazy # Импортируем функцию перенаправления

class UserLoginView(PageContextMixin, LoginView): # Для рендеринга страницы входа
    page_url = 'login' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    template_name = 'usersapp/login.html' # Указываем шаблон

class UserCreateView(PageContextMixin, CreateView): # Для рендеринга страницы регистрации нового пользователя
    page_url = 'register' # Создаём наследованный из ContextMixin контекст из записи таблицы Page
    model = SiteUser # Указываем модель
    template_name = 'usersapp/register.html' # Указываем шаблон
    form_class = RegistrationForm # Указываем форму регистрации
    success_url = reverse_lazy('usersapp:login') # Указываем адрес перенаправления при успешной регистрации