from django.contrib.auth.views import LoginView # Импортируем класс для авторизации
from .forms import RegistrationForm # Импортируем форму регистрации
from django.views.generic import CreateView # Импортируем базовый класс для создания
from .models import SiteUser, SiteUserSerializer # Импортируем модель пользователя SiteUser и его сериализатор
from django.urls import reverse_lazy # Импортируем функцию перенаправления
from rest_framework import viewsets # Импортируем viewsets для создания представлений на основе моделей

class UserLoginView(LoginView): # Для рендеринга страницы входа
    template_name = 'usersapp/login.html' # Указываем шаблон

class UserCreateView(CreateView): # Для рендеринга страницы регистрации нового пользователя
    model = SiteUser # Указываем модель
    template_name = 'usersapp/register.html' # Указываем шаблон
    form_class = RegistrationForm # Указываем форму регистрации
    success_url = reverse_lazy('usersapp:login') # Указываем адрес перенаправления при успешной регистрации

class SiteUserViewSet(viewsets.ModelViewSet): # Создаём ViewSet для модели в этом же файле, поскольку очень мало тут, не запутаюсь, надеюсь, в будущем
    queryset = SiteUser.objects.all() # Определяем queryset, который будет возвращать все объекты модели
    serializer_class = SiteUserSerializer # Указываем сериализатор, который будет использоваться для преобразования данных модели