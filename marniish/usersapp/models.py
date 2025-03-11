from django.db import models # Импорт функционирования моделей
from django.contrib.auth.models import AbstractUser # Абстрактный, чтобы он не создавался в БД, наследовался для создания модели интерактивного добавления нового ползователя
from rest_framework import serializers # Загружаем метод работы с сериализаторами

# Для проекта необходимости не вижу, но пусть будет в учебных целях до публикации на сервере
class SiteUser(AbstractUser): # Нужно в начале проекта всегда его создавать, чтобы была возможность изменения работы с пользователями и не пришлось проблемно пересоздавать БД после того, как сделали своего пользователя
    email = models.EmailField(unique=True) # Иначе стандартное поле email не уникальное

    def save(self, *args, **kwargs):  # Переопределяем метод сохранения нового пользователя
        if not self.pk: # Проверяем, что пользователь новый (еще не сохранен в базе)
            self.is_active = False # Чтобы новые пользователи были неактивными
        super().save(*args, **kwargs)  # Сохраняем пользователя
        if not Profile.objects.filter(user=self).exists():  # Если профиль не существует
            Profile.objects.create(user=self)  # То создаем профиль

# Для проекта необходимости не вижу, но пусть будет в учебных целях до публикации на сервере
class Profile(models.Model): # При создании нового пользователя будет создаваться профиль Profile
    false_true = models.BooleanField(default=True) # Чисто для галочки будет такое поле
    user = models.OneToOneField(SiteUser, on_delete=models.CASCADE) # Связь с пользователем будет такой

''' Вариант с применением сигнала вместо def save, если в будущем понадобится (не рекомендуется)
@receiver(post_save, sender=SiteUser) # Сигнал, который будет вызываться после создания пользователя
def create_profile(sender, instance, **kwargs): # Функция, которая будет вызываться после создания пользователя
    if not Profile.objects.filter(user=instance).exists(): # Если профиль не существует
        Profile.objects.create(user=instance) # То создаем профиль
'''

class SiteUserSerializer(serializers.HyperlinkedModelSerializer): # Создаём сериализатор для модели в файле моделей, поскольку очень мало тут, не запутаюсь, надеюсь
    class Meta:
        model = SiteUser # Указываем модель
        fields = ['id', 'username', 'email', 'first_name', 'last_name',
                  'is_superuser', 'last_login', 'is_staff', 'is_active', 'date_joined']  # Оставляем только нужные поля (иначе ошибка)