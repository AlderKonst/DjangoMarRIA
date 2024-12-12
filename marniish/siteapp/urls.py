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
from siteapp import views # Импортируем представления из приложения siteapp
from django.conf import settings # Импортируем настройки Django
from django.conf.urls.static import static # Импортируем функцию для работы со статическими файлами

urlpatterns = [
    path('', views.index, name='index'), # Главная страница
    path('News2024/', views.news2024, name='News2024'), # Новости за 2024 год
    path('News2023/', views.news2023, name='News2023'), # Новости за 2023 год
    path('News2022/', views.news2022, name='News2022'), # Новости за 2022 год
    path('News2021/', views.news2021, name='News2021'), # Новости за 2021 год
    path('News2020/', views.news2020, name='News2020'), # Новости за 2020 год
    path('News2019/', views.news2019, name='News2019'), # Новости за 2019 год
    path('News2018/', views.news2018, name='News2018'), # Новости за 2018 год
    path('News2017/', views.news2017, name='News2017'), # Новости за 2017 год
    path('News2016/', views.news2016, name='News2016'), # Новости за 2016 год
    path('Prod/', views.prod, name='Prod'), # Продукция
    path('Grain/', views.grain, name='Grain'), # Зерновые
    path('Potato/', views.potato, name='Potato'), # Картофель
    path('Grass/', views.grass, name='Grass'), # Многолетние травы
    path('Jim/', views.jim, name='Jim'), # Жимолость
    path('About/', views.about, name='About'), # История института
    path('Trend/', views.trend, name='Trend'), # Направления деятельности
    path('Progress/', views.progress, name='Progress'), # Достижения
    path('Article/', views.article, name='Article'), # Статьи
    path('Contact/', views.contact, name='Contact'), # Контакты
    path('Price/', views.price, name='Price'), # Прайс
    path('Docs/', views.docs, name='Docs'), # Документы
    path('Map/', views.mapping, name='Map'), # Карта сайта
    path('<str:url>/', views.this_page, name='this_page'), # Текущая страница
    path('<str:parent_url>/', views.parent_page, name='parent_page'), # Страница родителя
    # path('News/<int:id>/', views.news, name='News'), # Новости
]

if settings.DEBUG: # Чтобы изображения могли отображаться в браузере
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)