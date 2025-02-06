from django.test import TestCase # Импортируем тесты из модуля django.test
from mixer.backend.django import mixer # Импортируем миксер
from .models import *  # Загружаем моделей

class SiteUserTestCase(TestCase): # Проверка правильности создания пользователя
    def setUp(self): # Для каждого метода
        self.email = 'test@example.com' # Определяем email для использования в тестах
        self.password = 'password123' # пароль
        self.username1 = 'user1' # имя первого
        self.username2 = 'user2' # и второго пользователя
        self.user = SiteUser.objects.create_user(username=self.username1, email=self.email, password=self.password) # Создаём первого пользователя
    def test_unique_email(self): # Для проверки попытки создания 2-го пользователя с тем же email
        with self.assertRaises(Exception): # Ожидаем ошибку, так как email должен быть уникальным
            SiteUser.objects.create_user(username=self.username2, email=self.email, password=self.password) # Пытаемся создать 2-го пользователя с тем же email
    def test_profile_creation(self): # Создаётся ли автомитически профиль пользователя?
        self.assertTrue(Profile.objects.filter(user=self.user).exists()) # Существует ли автоматически созданный профиль?

class ProfileTestCase(TestCase): # Проверка правильности создания связанного с пользователем профиля
    def setUp(self): # Для каждого метода
        self.user = mixer.blend(SiteUser) # Создаём пользователя
        self.profile = Profile.objects.get(user=self.user) # Получаем связанный профиль
    def test_profile_creation(self): # Для проверки связанности созданного профиля с тем же созданным пользловаталем
        self.assertEqual(self.profile.user, self.user) # Профиль связан с тем же пользователем?
    def test_false_true_default(self): # Правильно ли работает значение по умолчания для поля false_true?
        self.assertTrue(self.profile.false_true) # Поле false_true по умолчанию остаётся ли True?