from django.test import Client
from django.test import TestCase
from mixer.backend.django import mixer # Импортируем миксер
from .models import Page, News, CultureGroup, Trend, Progress
from usersapp.models import SiteUser

urls = [ # Все пути не требующих прав, кроме 'page' (он вспомогательный, лишь для отображения пути в HTML)
    '',
    'News_last/',
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
urls_aaa = [ # Все пути, требующие права
    '/News/editing/',
    *[f'/News/update/{year}/' for year in range(2015, 2030)],
    *[f'/News/delete/{year}/' for year in range(2015, 2030)],
    '/News/News_picture/editing/',
    *[f'/News/News_picture/update/{year}/' for year in range(2015, 2030)],
    *[f'/News/News_picture/delete/{year}/' for year in range(2015, 2030)],
    '/Taxon/editing/',
    *[f'/Taxon/update/{i}/' for i in range(1, 25)],
    *[f'/Taxon/delete/{i}/' for i in range(1, 25)],
    '/Culture/editing/',
    *[f'/Culture/update/{i}/' for i in range(1, 10)],
    *[f'/Culture/delete/{i}/' for i in range(1, 10)],
    '/Culture_group/editing/',
    *[f'/Culture_group/update/{i}/' for i in range(1, 5)],
    '/About/editing',
    *[f'/About/delete/{i}/' for i in range(1, 10)],
    *[f'/About/update/{i}/' for i in range(1, 10)],
    '/Trend/editing/',
    *[f'/Trend/update/{i}/' for i in range(1, 5)],
    *[f'/Trend/delete/{i}/' for i in range(1, 5)],
    '/Progress/editing',
    *[f'/Progress/update/{i}/' for i in range(1, 15)],
    *[f'/Progress/delete/{i}/' for i in range(1, 15)],
    '/Article/editing/',
    *[f'/Article/update/{i}/' for i in range(1, 20)],
    *[f'/Article/delete/{i}/' for i in range(1, 20)],
    '/Price/editing/',
    *[f'/Price/update/{i}/' for i in range(1, 10)],
    *[f'/Price/delete/{i}/' for i in range(1, 10)],
    '/Category/editing/',
    *[f'/Category/update/{i}/' for i in range(1, 10)],
    *[f'/Category/delete/{i}/' for i in range(1, 10)],
    '/Docs/editing/',
    *[f'/Docs/delete/{i}/' for i in range(1, 20)],
    *[f'/Docs/update/{i}/' for i in range(1, 20)],
]
culture_groups = { # Чтобы создавать записи CultureGroup
    'Grain/': 'Зерновые культуры',
    'Potato/': 'Клубнеплоды',
    'Grass/': 'Многолетние травы',
    'Jim/': 'Плодово-ягодные культуры',
}

class ViewsTest(TestCase): # Определяем класс тестов, наследующий от TestCase
    def setUp(self): # Для выполнения перед каждым тестом
        self.client = Client() # Создаём экземпляр клиента для выполнения запросов
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

    def test_aaa(self): # Метод для тестирования страниц с правами
        SiteUser.objects.create_user(username='mari', email='mari@nii.ru', password='mari0nii0ru')
        self.client.login(username='mari', password='mari0nii0ru')

        Page.objects.create(url='News_editing', title='News_editing')
        response = self.client.get('/News/editing/')
        self.assertEqual(response.status_code, 200)

        news_one = News.objects.create(date='2015-01-01', title='News', text='News')
        Page.objects.create(url='News_update', title='News_update')
        response = self.client.get(f'/News/update/{news_one.pk}/')
        self.assertEqual(response.status_code, 200)

        Page.objects.create(url='News_picture_editing', title='News_picture_editing')
        response = self.client.get('/News/News_picture/editing/')
        self.assertEqual(response.status_code, 200)

        Page.objects.create(url='Taxon_editing', title='Taxon_editing')
        response = self.client.get('/Taxon/editing/')
        self.assertEqual(response.status_code, 200)

        Page.objects.create(url='Culture_editing', title='Culture_editing')
        response = self.client.get('/Culture/editing/')
        self.assertEqual(response.status_code, 200)

        Page.objects.create(url='Culture_group_editing', title='Culture_group_editing')
        response = self.client.get('/Culture_group/editing/')
        self.assertEqual(response.status_code, 200)

        Page.objects.create(url='About_editing', title='About_editing')
        response = self.client.get('/About/editing/')
        self.assertEqual(response.status_code, 200)

        Page.objects.create(url='Trend_editing', title='Trend_editing')
        response = self.client.get('/Trend/editing/')
        self.assertEqual(response.status_code, 200)

        Trend.objects.create(name='plant') # Почему только если значение 'plant' работает, а 'zoo', 'bird' и 'land' нет? Безумие!
        Page.objects.create(url='Progress_editing', title='Progress_editing')
        response = self.client.get('/Progress/editing/')
        self.assertEqual(response.status_code, 200)

        Page.objects.create(url='Article_editing', title='Article_editing')
        response = self.client.get('/Article/editing/')
        self.assertEqual(response.status_code, 200)

        Page.objects.create(url='Price_editing', title='Price_editing')
        response = self.client.get('/Price/editing/')
        self.assertEqual(response.status_code, 200)

        Page.objects.create(url='Category_editing', title='Category_editing')
        response = self.client.get('/Category/editing/')
        self.assertEqual(response.status_code, 200)

        Page.objects.create(url='Docs_editing', title='Docs_editing')
        response = self.client.get('/Docs/editing/')
        self.assertEqual(response.status_code, 200)