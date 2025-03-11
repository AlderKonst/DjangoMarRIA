from django.test import Client
from django.test import TestCase
from mixer.backend.django import mixer # Импортируем миксер
from .models import Page, News, CultureGroup, Trend, Progress, NewsPicture, Taxon, Culture, History, TrendItem, Article, \
    Price, ProdCategory, Document
from usersapp.models import SiteUser

urls = [ # Все пути не требующих прав, кроме 'page' (он вспомогательный, лишь для отображения пути в HTML)
    '',
    'Newses/',
    *[f'{year}/' for year in range(2015, 2030)],
    'Prod/',
    'Grain/',
    'Potato/',
    'Grass/',
    'Jim/',
    'About/',
    'Trend/',
    'Progress/',
    'Article/',
    'Contact/',
    'Price/',
    'Docs/',
    'Map/'
]
culture_groups = { # Чтобы создавать записи CultureGroup
    'Grain/': 'Зерновые культуры',
    'Potato/': 'Клубнеплоды',
    'Grass/': 'Многолетние травы',
    'Jim/': 'Плодово-ягодные культуры',
}
models_prefix = [ # Список кортежей из названия модели и префикса URL сайта
    (News, 'News'),
    (NewsPicture, 'News_picture'),
    (Taxon, 'Taxon'),
    (Culture, 'Culture'),
    (CultureGroup, 'Culture_group'),
    (History, 'About'),
    (TrendItem, 'Trend'),
    (Progress, 'Progress'),
    (Article, 'Article'),
    (Price, 'Price'),
    (ProdCategory, 'Category'),
    (Document, 'Docs')
]

class ViewsTest(TestCase): # Определяем класс тестов, наследующий от TestCase

    def setUp(self): # Для выполнения перед каждым тестом
        self.client = Client() # Создаём экземпляр клиента для выполнения запросов
        SiteUser.objects.create_user(username='mari', email='mari@nii.ru', password='mari0nii') # Создаём пользователя тестового
        Trend.objects.create(name='plant') # Почему только если значение 'plant' работает, а 'zoo', 'bird' и 'land' нет? Безумие!

    def test_statuses(self): # Метод для тестирования статуса 200 страниц
        for url, name in culture_groups.items(): # Проходим по всем элементам словаря culture_groups
            CultureGroup.objects.create(name=name) # Создаём объект CultureGroup с названием группы культур

        for url in urls: # Проходим по всем URL из списка urls
            url_name = url.replace('/', '') or 'index' # Убираем '/' из URL и используем 'index', если URL пустой
            Page.objects.create(url=url_name, title=url_name) # Создаём объект Page с URL и заголовком
            if url_name.isdigit(): # Проверяем, является ли URL числом (годы новости)
                response = self.client.get(f'/News/{url_name}/') # Выполняем GET-запрос к странице новостей по числовому URL
            else: # Если URL не является числом (все остальные пути)
                response = self.client.get(f'/{url}') # Выполняем GET-запрос к указанному URL
            self.assertEqual(response.status_code, 200) # Проверяем, что статус ответа равен 200 (ОК)

    def aaa(self, is_authenticated=False): # Общий метод для тестирования страниц с правами, без доступа по-умолчанию
        if is_authenticated: # Если пользователь авторизован
            self.client.login(username='mari', password='mari0nii') # Выполняем авторизацию
            status_code = 200 # При этом статус ответа делаем 200
        else: # Если же нет
            status_code = 302 # То статус ответа делаем 302 (Отказано в доступе)

        for model, url_prefix in models_prefix: # Итерируемся по списку моделей и префиксов URL
            base_url = url_prefix # Инициализируем базовый URL текущим префиксом (почти для всех случаев)
            if model == NewsPicture: # Если текущая модель NewsPicture
                base_url = 'News/News_picture' # То изменяем базовый URL на 'News/News_picture'

            mixer.blend(Page, url=f'{url_prefix}_editing') # Создаём страницу для редактирования с URL, сформированным из префикса
            response = self.client.get(f'/{base_url}/editing/') # Выполняем GET-запрос к странице редактирования
            self.assertEqual(response.status_code, status_code) # Проверяем, что код ответа

            obj = mixer.blend(model) # Создаём объект текущей модели
            mixer.blend(Page, url=f'{url_prefix}_update') # Создаём страницу для обновления (изменения) записи
            response = self.client.get(f'/{base_url}/update/{obj.pk}/') # Выполняем GET-запрос к странице обновления объекта
            self.assertEqual(response.status_code, status_code) # Проверяем, что код ответа

            if model != CultureGroup: # Удаляем только если текущая модель не относится к CultureGroup?
                obj = mixer.blend(model) # Создаём еще один объект текущей модели (для удаления)
                mixer.blend(Page, url=f'{url_prefix}_delete') # Создаём страницу для удаления объекта
                response = self.client.get(f'/{base_url}/delete/{obj.pk}/') # Выполняем GET-запрос к странице удаления объекта
                self.assertEqual(response.status_code, status_code) # Проверяем код

    def test_no_aaa(self): # Проверяем страницы при неавторизованном пользователе
        self.aaa(is_authenticated=False) # На всякий случай значение с аргументом устанавливаю

    def test_post(self): # Проверю на POST-запрос только самый мудрёный, остальные не стоят того, получится слишком много кода проверять поля каждого представления
        response = self.client.post('/Contact/', {'name': 'Саша', 'email': 'mari@nii.ru', 'subject': '', 'message': 'Сообщение'})
        self.assertEqual(response.status_code, 302) # Если отправились данные правильно, то код ответа должен быть 302 (редирект)