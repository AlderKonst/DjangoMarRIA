from django.contrib.auth.views import LoginView # Импортируем класс для авторизации
from .forms import RegistrationForm # Импортируем форму регистрации
from django.views.generic import CreateView, DetailView  # Импортируем базовый класс для создания и детализации записи
from .models import SiteUser, SiteUserSerializer # Импортируем модель пользователя SiteUser и его сериализатор
from django.urls import reverse_lazy, reverse # Импортируем функцию перенаправления
from rest_framework import viewsets # Импортируем viewsets для создания представлений на основе моделей
from rest_framework.authtoken.models import Token # Импортируем автоматически созданную модель токена
from django.shortcuts import HttpResponseRedirect # Импортируем отправку обработанного ответа на страницу
# from django.http import JsonResponse # Импортируем отправку обработанного ответа на страницу в виде JSON (если будет использоваться AJAX)

class UserLoginView(LoginView): # Для рендеринга страницы входа
    template_name = 'usersapp/login.html' # Указываем шаблон

class UserCreateView(CreateView): # Для рендеринга страницы регистрации нового пользователя
    model = SiteUser # Указываем модель
    template_name = 'usersapp/register.html' # Указываем шаблон
    form_class = RegistrationForm # Указываем форму регистрации
    success_url = reverse_lazy('usersapp:login') # Указываем адрес перенаправления при успешной регистрации
    def form_valid(self, form): # Для переопределения в случае валидности
        response = super().form_valid(form) # Получаем ответ с правильными данными формы
        Token.objects.create(user=self.object) # Создаём токен для нового пользователя (при создании)
        return response # Возвращаем ответ

class SiteUserViewSet(viewsets.ModelViewSet): # Создаём ViewSet для модели в этом же файле, поскольку очень мало тут, не запутаюсь, надеюсь, в будущем
    queryset = SiteUser.objects.all() # Определяем queryset, который будет возвращать все объекты модели
    serializer_class = SiteUserSerializer # Указываем сериализатор, который будет использоваться для преобразования данных модели

class UserDetailView(DetailView): # Чтобы токен мог создать пользователь себе
    template_name = 'usersapp/user_token.html' # Указываем шаблон
    model = SiteUser # Указываем модель

def update_token(request): # Создание и обновление токена
    user = request.user # Получаем пользователя по GET-запросу
    if user.auth_token: # Если уже токен есть, то обновляем его
        user.auth_token.delete() # через удаление
        Token.objects.create(user=user) # и создание
    else: # Если же нет
        Token.objects.create(user=user) # то создаём
    return HttpResponseRedirect(reverse('usersapp:user_token', kwargs={'pk': user.pk})) # Отправляем на страницу данные

""" На будущее, если понадобится
def update_token_ajax(request): # Обновление токена с помощью AJAX (кнопка ниже)
    user = request.user # Получаем пользователя по GET-запросу
    if user.auth_token: # Если уже токен есть, то обновляем его
        user.auth_token.delete() # через удаление
        token = Token.objects.create(user=user) # и создание
    else: # Если же нет
        token = Token.objects.create(user=user) # то создаём
    return JsonResponse({'key': token.key}) # Передаём данные в виде AJAX
"""