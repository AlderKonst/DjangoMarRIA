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

app_name = 'siteapp' # Задаем имя приложения для использования в пространстве имен

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),  # Главная страница
    path('News/<int:year>/', views.NewsListView.as_view(), name='News'), # Добавляем пути для новостей за каждый год
    path('Prod/', views.ProdTemplateView.as_view(), name='Prod'), # Продукция
    path('Grain/', views.GrainTemplateView.as_view(), name='Grain'), # Зерновые
    path('Potato/', views.PotatoTemplateView.as_view(), name='Potato'), # Картофель
    path('Grass/', views.GrassTemplateView.as_view(), name='Grass'), # Многолетние травы
    path('Jim/', views.JimTemplateView.as_view(), name='Jim'), # Жимолость
    path('About/', views.AboutTemplateView.as_view(), name='About'), # История института
    path('Trend/', views.TrendListView.as_view(), name='Trend'), # Направления деятельности
    path('Trend/editing/', views.TrendEditingView.as_view(), name='Trend_editing'), # Редактирование направлений деятельности
    path('Trend/edit/<int:pk>/', views.TrendEditUpdateView.as_view(), name='Trend_edit'), # Изменение направления деятельности
    path('Trend/delete/<int:pk>/', views.TrendDeleteView.as_view(), name='Trend_delete'), # Удаление направления деятельности
    path('Progress/', views.ProgressListView.as_view(), name='Progress'), # Достижения
    path('Article/', views.ArticleListView.as_view(), name='Article'), # Статьи
    path('Contact/', views.ContactTemplateView.as_view(), name='Contact'), # Контакты
    path('Price/', views.PriceListView.as_view(), name='Price'), # Прайс
    path('Docs/', views.DocsListView.as_view(), name='Docs'), # Документы
    path('Docs/editing/', views.DocsEditingView.as_view(), name='Docs_editing'), # Редактирование документов
    path('Docs/delete/<int:pk>/', views.DocsDeleteView.as_view(), name='Docs_delete'), # Подтверждение удаления документа
    path('Docs/edit/<int:pk>/', views.DocsEditUpdateView.as_view(), name='Docs_edit'), # Изменение
    path('Map/', views.MapTemplateView.as_view(), name='Map'), # Карта сайта
    path('<str:url>/', views.ThisPageListView.as_view(), name='this_page'), # Текущая страница
    path('<str:parent_url>/', views.ParentPageListView.as_view(), name='parent_page'), # Страница родителя
]

if settings.DEBUG: # Чтобы изображения могли отображаться в браузере
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)