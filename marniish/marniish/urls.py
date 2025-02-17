"""
В этом коде мы настраиваем URL-маршруты для нашего проекта marniish. Список urlpatterns направляет URL-адреса на представления. Для получения дополнительной информации см.:
https://docs.djangoproject.com/en/5.1/topics/http/urls/
Примеры:
Функциональные представления
1. Добавьте импорт: from my_app import views
2. Добавьте URL в urlpatterns: path('', views.home, name='home')
Классовые представления
1. Добавьте импорт: from other_app.views import Home
2. Добавьте URL в urlpatterns: path('', Home.as_view(), name='home')
Включение другой URL-конфигурации
1. Импортируйте функцию include(): from django.urls import include, path
2. Добавьте URL в urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # Импортируем модуль администрирования Django
from django.urls import path, include  # Импортируем функции для работы с URL-адресами
from django.conf import settings # Импортируем настройки Django
from django.conf.urls.static import static # Импортируем функцию для работы со статическими файлами

urlpatterns = [  # Определяем список маршрутов (URL-шаблонов)
    path('admin/', admin.site.urls),  # Маршрут для доступа к административной панели Django
    path('users/', include(('usersapp.urls', 'usersapp'), namespace='usersapp')),  # Маршрут страниц по ААА
    path('', include(('siteapp.urls', 'siteapp'), namespace='siteapp')),  # Включаем маршруты из файла siteapp.urls с пространством имен 'siteapp'
]

if settings.DEBUG: # Чтобы изображения могли отображаться в браузере
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)