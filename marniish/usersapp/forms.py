from django.contrib.auth.forms import UserCreationForm # Импортируем класс для переопределения формы регистрации
from .models import SiteUser

class RegistrationForm(UserCreationForm): # Тут есть двойное введение пароли и их проверка на идеинтичность
    class Meta:
        model = SiteUser
        fields = ('username', 'password1', 'password2', # Эти поля и так есть, стандартные
                  'email') # Пусть ещё будет email