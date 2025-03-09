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
from debug_toolbar.toolbar import debug_toolbar_urls # Импортируем urls модуль из debug_toolbar
from django.conf import settings # Импортируем настройки Django
from django.conf.urls.static import static # Импортируем функцию для работы со статическими файлами
from rest_framework import routers # Импортируем модуль для работы с маршрутами API
from usersapp.views import SiteUserViewSet # Импортируем необходимый из-за 'newsew' ViewSet для API
from siteapp.api_views import * # Импортируем все ViewSet'ы для API

router = routers.DefaultRouter() # Создание экземпляра DefaultRouter для управления маршрутами API
router.register(r'siteusers', SiteUserViewSet) # Регистрация ViewSet по маршруту 'users'
router.register(r'trends', TrendViewSet) # Регистрация ViewSet по маршруту 'trends'
router.register(r'articles', ArticleViewSet) # Регистрация ViewSet по маршруту 'articles'
router.register(r'progresses', ProgressViewSet) # Регистрация ViewSet по маршруту 'progresses'
router.register(r'pages', PageViewSet) # Регистрация ViewSet по маршруту 'pages'
router.register(r'trenditems', TrendItemViewSet) # Регистрация ViewSet по маршруту 'trenditems'
router.register(r'references', ReferenceViewSet) # Регистрация ViewSet по маршруту 'references'
router.register(r'historydates', HistoryDataViewSet) # Регистрация ViewSet по маршруту 'historydates'
router.register(r'histories', HistoryViewSet) # Регистрация ViewSet по маршруту 'histories'
router.register(r'culturegroups', CultureGroupViewSet) # Регистрация ViewSet по маршруту 'culturegroups'
router.register(r'cultures', CultureViewSet) # Регистрация ViewSet по маршруту 'cultures'
router.register(r'taxons', TaxonViewSet) # Регистрация ViewSet по маршруту 'taxons'
router.register(r'documents', DocumentViewSet) # Регистрация ViewSet по маршруту 'documents'
router.register(r'prodcategories', ProdCategoryViewSet) # Регистрация ViewSet по маршруту 'prodcategories'
router.register(r'prices', PriceViewSet) # Регистрация ViewSet по маршруту 'prices'
router.register(r'newspictures', NewsPictureViewSet) # Регистрация ViewSet по маршруту 'newspictures'
router.register(r'newses', NewsViewSet) # Регистрация ViewSet по маршруту 'newses'

urlpatterns = [  # Определяем список маршрутов (URL-шаблонов)
    path('admin/', admin.site.urls),  # Маршрут для доступа к административной панели Django
    path('users/', include(('usersapp.urls', 'usersapp'), namespace='usersapp')),  # Маршрут страниц по ААА
    path('', include(('siteapp.urls', 'siteapp'), namespace='siteapp')),  # Включаем маршруты из файла siteapp.urls с пространством имен 'siteapp'
    path('api/v0/', include(router.urls)), # Путь доступа через API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # Для работы с API
] + debug_toolbar_urls() # В отличие от старых версий Django, проще и добавляем не в блок "if settings.DEBUG"

if settings.DEBUG: # Чтобы изображения могли отображаться в браузере
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)