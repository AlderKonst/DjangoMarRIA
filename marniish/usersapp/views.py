from django.contrib.auth.views import LoginView # Импортируем базовый класс для входа
from .forms import RegistrationForm # Импортируем форму регистрации
from django.views.generic import CreateView # Импортируем базовый класс для создания
from .models import SiteUser # Импортируем модель пользователя SiteUser
from django.urls import reverse_lazy # Импортируем функцию перенаправления

class UserLoginView(LoginView): # Для рендеринга страницы входа
    template_name = 'usersapp/login.html' # Указываем шаблон

class UserCreateView(CreateView): # Для рендеринга страницы регистрации нового пользователя
    model = SiteUser # Указываем модель
    template_name = 'usersapp/register.html' # Указываем шаблон
    form_class = RegistrationForm # Указываем форму регистрации
    success_url = reverse_lazy('users:login') # Указываем адрес перенаправления при успешной регистрации