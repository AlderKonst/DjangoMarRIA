"""
Конфигурация URL для проекта блога.

Список urlpatterns перенаправляет URL-адреса на представления. Для получения дополнительной информации см.:
https://docs.djangoproject.com/en/5.1/topics/http/urls/
Примеры:
Функциональные представления
1. Добавьте импорт: from my_app import views
2. Добавьте URL в urlpatterns: path('', views.home, name='home')
Классовые представления
1. Добавьте импорт: from other_app.views import Home
2. Добавьте URL в urlpatterns: path('', Home.as_view(), name='home')
Включение другой URLconf
1. Импортируйте функцию include(): from django.urls import include, path
2. Добавьте URL в urlpatterns: path('blog/', include('blog.urls'))
"""

from django.urls import path # Импортируем функцию для определения URL-маршрутов
from usersapp import views # Импортируем представления из приложения usersapp
from django.contrib.auth.views import LogoutView # Импортируем представление для выхода

app_name = 'usersapp' # Задаем имя приложения для использования в пространстве имен

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'), # Страница авторизации (входа)
    path('logout/', LogoutView.as_view(), name='logout'), # Выход
    path('register/', views.UserCreateView.as_view(), name='register'), # Страница регистрации нового пользователя
    path('user_token/<int:pk>', views.UserDetailView.as_view(), name='user_token'), # Страница с профилем пользователя для генерации токена
    path('update_token/', views.update_token, name='update_token'), # Для создания токена по кнопке без JavaScript
    #path('update_token_ajax/', views.update_token_ajax), # Для создания токена по кнопке JavaScript-ом (на будущее рассмотрение)
]