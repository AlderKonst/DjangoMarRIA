from django.test import TestCase # Импортируем тесты из модуля django.test
from mixer.backend.django import mixer # Импортируем миксер
from .models import *  # Загружаем моделей
from usersapp.models import SiteUser # Загружаем ещё и модель с приложения с пользователями

class TrendTestCase(TestCase): # Проверка для модели Trend
    def test_verbose_names(self): # Проверка на соответствие имён verbose_name и verbose_name_plural (только на раз)
        self.assertEqual(Trend._meta.verbose_name, 'Основное направление деятельности')
        self.assertEqual(Trend._meta.verbose_name_plural, 'Основные направления деятельности')

    def test_trend_creation(self): # Проверка создания модели Trend
        trend = mixer.blend(Trend, name='Trend') # Создаём модель Trend
        self.assertEqual(trend.name, 'Trend') # С таким же именем он создался?

class BaseTrendTestCase(TestCase): # Создание базового теста для моделей Trend
    def setUp(self): # Для выполнения перед каждым тестом
        self.trend = mixer.blend(Trend) # Создаем экземпляр объекта Trend с помощью mixer

class ArticleTestCase(BaseTrendTestCase): # Проверка для модели Article
    def create_article(self, doi='', link='', name='article', year=2024): # Для создания статьи с параметрами по умолчанию
        return mixer.blend(Article, trend=self.trend, name=name, year=year, doi=doi, link=link) # Возвращаем экземпляр Article с заданными параметрами
    def test_article_creation(self): # Для проверки создания статьи
        article = self.create_article() # Создаем статью с параметрами по умолчанию
        self.assertEqual(article.trend, self.trend) # Проверяем, что тренд статьи такой же
        self.assertEqual(article.name, 'article') # Проверяем, что имя статьи соответствующая
        self.assertEqual(article.year, 2024) # Проверяем, что год статьи соответствует ожидаемому
    def test_get_doi_url_doi(self): # Для проверки получения DOI
        article = self.create_article(doi='10.1000/test') # Создаем статью с заданным DOI
        self.assertEqual(article.get_doi_url(), "DOI: 10.1000/test") # Проверяем, что метод возвращает тот же DOI
    def test_get_doi_url_link(self): # Для проверки получения URL ссылки
        article = self.create_article(link='https://example.com') # Создаем статью с заданной ссылкой
        self.assertEqual(article.get_doi_url(), "URL: https://example.com") # Метод возвращает правильный URL ссылки?
    def test_get_doi_url_empty(self): # Для проверки поведения при отсутствии DOI и URL
        article = self.create_article() # Создаем статью без DOI и ссылки
        self.assertEqual(article.get_doi_url(), "") # Метод возвращает пустую строку?

class ProgressTestCase(BaseTrendTestCase): # Проверка для модели Progress
    def test_progress_creation(self): # Для проверки создания достижения
        progress = mixer.blend(Progress, trend=self.trend) # Создаем запись с достижением
        self.assertEqual(progress.trend, self.trend) # Проверяем, что направление деятельности соответствует в достижении

class PageTestCase(TestCase): # Проверка для модели Page
    def test_page_creation(self): # Для проверки создания страницы
        page = mixer.blend(Page) # Создаем экземпляр модели Page с помощью mixer
        self.assertTrue(isinstance(page, Page)) # Проверяем, что созданный объект является экземпляром класса Page

class TrendItemTestCase(BaseTrendTestCase): # Проверка для модели TrendItem
    def test_trend_item_creation(self): # Для проверки создания пункта направления деятельности
        trend_item = mixer.blend(TrendItem, trend=self.trend) # Создаем запись с пунктом направления деятельности
        self.assertEqual(trend_item.trend, self.trend) # Проверяем, что направление деятельности соответствует в пункте направления деятельности

class ReferenceTestCase(TestCase): # Проверка для модели Reference
    def test_reference_creation(self): # Для проверки создания полезной ссылки
        reference = mixer.blend(Reference) # Создаем экземпляр модели Reference с помощью mixer
        self.assertTrue(isinstance(reference, Reference)) # Проверяем, что созданный объект является экземпляром класса Reference

class HistoryDataTest(TestCase): # Проверка для модели HistoryData
    def test_get_histories(self): # Проверка метода get_histories, возвращающего связанные History
        history_data = mixer.blend(HistoryData) # Создаём экземпляр HistoryData с помощью mixer (создается случайный экземпляр)
        for _ in range(3): # Создаём 3 связанных экземпляра History для данного HistoryData
            mixer.blend(History, data=history_data) # Связываем History с созданным HistoryData через внешний ключ data
        self.assertEqual(history_data.get_histories().count(), 3) # Проверяем, что метод get_histories возвращает 3 связанных записи с History

class HistoryTest(TestCase): # Проверка для модели History
    def test_history_creation(self): # Для проверки создания связанной записи History
        history_data = mixer.blend(HistoryData) # Создаём экземпляр HistoryData с помощью mixer
        history = mixer.blend(History, data=history_data, text="Test history") # Связываем History с созданным HistoryData через внешний ключ data
        self.assertEqual(str(history), "Test history") # Проверяем, что метод __str__ возвращает текст связанной записи

class CultureGroupTest(TestCase): # Проверка для модели CultureGroup
    def test_get_cultures(self): # Проверка метода get_cultures, возвращающего связанные Culture
        culture_group = mixer.blend(CultureGroup) # Создаём экземпляр CultureGroup с помощью mixer
        cultures = mixer.cycle(3).blend(Culture, group=culture_group) # 3 раза создаём Culture через внешний ключ group миксером
        self.assertEqual(list(culture_group.get_cultures()), list(cultures)) # Проверяем, что методом get_cultures возвращается точно такой же список связанных Culture

class CultureTest(TestCase): # Проверка для модели Culture
    def test_get_taxons(self): # Проверка метода get_taxons, возвращающего связанные Taxon
        culture_group = mixer.blend(CultureGroup) # Создаём экземпляр CultureGroup с помощью mixer
        culture = mixer.blend(Culture, group=culture_group) # Связываем Culture с созданным CultureGroup через внешний ключ group миксером
        taxons = mixer.cycle(3).blend(Taxon, culture=culture) # 3 раза создаём Taxon через внешний ключ culture миксером
        self.assertEqual(list(culture.get_taxons()), list(taxons)) # Проверяем, что методом get_taxons возвращается точно такой же список связанных Taxon

class TaxonTest(TestCase): # Проверка для модели Taxon
    def test_taxon_str(self): # Проверка метода __str__
        culture_group = mixer.blend(CultureGroup, name='group') # Создаём экземпляр CultureGroup с помощью mixer
        culture = mixer.blend(Culture, group=culture_group, name='culture') # Связываем Culture с созданным CultureGroup через внешний ключ group миксером
        taxon = mixer.blend(Taxon, culture=culture, name='taxon') # Связываем Taxon с созданным Culture через внешний ключ culture миксером
        self.assertEqual(str(taxon), 'culture taxon') # Возвращает ли метод __str__ текст связанной записи для админки

class DocumentTestCase(TestCase): # Проверка для модели Document
    def test_document_str(self): # Проверка метода __str__
        document = mixer.blend(Document, date='2024-07-27') # Создаём экземпляр Document с помощью mixer
        self.assertEqual(str(document), '27.07.2024') # Возвращает ли метод __str__ текст связанной записи для админки

class ProdCategoryTestCase(TestCase): # Проверка для модели ProdCategory
    def test_prod_category_creation(self): # Проверка создания категории продукции
        category = mixer.blend(ProdCategory) # Создаём экземпляр ProdCategory с помощью mixer
        self.assertTrue(isinstance(category, ProdCategory)) # Проверяем, что объект созданный в mixer является экземпляром класса ProdCategory

class PriceTestCase(TestCase): # Проверка для модели Price
    def test_price_creation(self): # Проверка создания записи с ценой продукции
        taxon = mixer.blend(Taxon, name="taxon") # Создаём экземпляр Taxon с помощью mixer
        category = mixer.blend(ProdCategory, name="category") # Создаём экземпляр ProdCategory с помощью mixer
        price = mixer.blend(Price, taxon=taxon, category=category, mass=10.5, price="1000") # Создаём экземпляр Price с помощью mixer с соответствующими связями
        self.assertTrue(isinstance(price, Price)) # Является ли объект, созданный в mixer, экземпляром класса Price
        self.assertEqual(str(price), "taxon") # Возвращает ли метод __str__ текст связанной записи для админки

class NewsPictureTestCase(TestCase): # Проверка для модели NewsPicture
    def test_news_picture_str(self): # Проверка метода __str__
        news_picture = mixer.blend(NewsPicture, alt='image') # Создаём экземпляр NewsPicture с помощью mixer
        self.assertEqual(str(news_picture), 'image') # Возвращает ли метод __str__ текст связанной записи для админки

class NewsTestCase(TestCase): # Проверка для модели News
    def test_news_str(self): # Проверка метода __str__
        news = mixer.blend(News, date='2024-10-27', title='news') # Создаём тестовый объект News с помощью mixer
        self.assertEqual(str(news), '2024-10-27') # Проверяем, что метод __str__ возвращает ту же дату
    def test_get_image_count(self): # Проверка метода get_image_count
        news = mixer.blend(News) # Создаём запись News миксером
        pictures = mixer.cycle(3).blend(NewsPicture) # Создаём 3 записи NewsPicture
        news.img.set(pictures) # Связываем News с NewsPicture
        self.assertEqual(news.get_image_count(), 3) # Проверяем, что метод get_image_count возвращает правильное количество записей
    def test_news_user(self): # Проверка поля user
        user = mixer.blend(SiteUser) # Создаём пользователя через mixer
        news = mixer.blend(News, user=user) # Создаём новость с этим пользователем
        self.assertEqual(news.user, user) # Проверяем, что пользователь созданный в mixer является записью класса SiteUser

    def test_get_all_years(self): # Проверка работы метода get_all_years менеджера YearNewsManager
        mixer.blend(News, date='2022-01-01') # Создаём новость с первым годом
        mixer.blend(News, date='2023-01-01') # вторым
        mixer.blend(News, date='2024-01-01') # и третьим
        years = News.objects.get_all_years() # Получаем эти созданные записи, согласно методу созданного менеджера
        self.assertEqual(list(years), [2022, 2023, 2024]) # Метод get_all_years возвращает этот же диапазон годов?
