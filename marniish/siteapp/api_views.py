from rest_framework import viewsets # Импортируем viewsets для создания представлений на основе моделей
from rest_framework.authentication import SessionAuthentication, TokenAuthentication # Импортируем методы авторизации по API
from rest_framework.permissions import IsAdminUser # Импортируем разрешение на доступ к данным через API только для админа
from .permissions import ReadOnly # Импортируем собственное разрешение на чтение данных через API
from .models import * # Импортируем все модели из текущего приложения
from .serializers import * # И соответствующие сериализаторы

# Только для некоторых ViewSet-ов методы авторизации и разрешения по доступу данным через API будут переопределены (иначе зачем settings.py)

class TrendViewSet(viewsets.ModelViewSet): # Создаём ViewSet для модели с основными направлениями деятельности НИИ со стандартным доступом в settings.py
    queryset = Trend.objects.all() # Определяем queryset, который будет возвращать все объекты модели
    serializer_class = TrendSerializer # Указываем сериализатор, который будет использоваться для преобразования данных модели в JSON

class ArticleViewSet(viewsets.ModelViewSet): # Создаём ViewSet для модели с важными статьями НИИ со стандартным доступом в settings.py
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ProgressViewSet(viewsets.ModelViewSet): # Создаём ViewSet для модели с основными достижениями НИИ со стандартным доступом в settings.py
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

class PageViewSet(viewsets.ModelViewSet): # Создаём ViewSet для модели с инфой о страницах сайта НИИ
    authentication_classes = [SessionAuthentication, TokenAuthentication]  # Авторизация по API будет ещё включать через токен
    permission_classes = [IsAdminUser | ReadOnly]  # Доступ к изменению данных через API есть только у админа, для остальных лишь чтение
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class TrendItemViewSet(viewsets.ModelViewSet): # Создаём ViewSet для модели с пунктами направлений деятельности НИИ
    authentication_classes = [SessionAuthentication, TokenAuthentication] # Авторизация по API будет ещё включать через токен
    permission_classes = [IsAdminUser | ReadOnly]  # Доступ к изменению данных через API есть только у админа, для остальных лишь чтение
    queryset = TrendItem.objects.all()
    serializer_class = TrendItemSerializer

class ReferenceViewSet(viewsets.ModelViewSet): # Создаём ViewSet для модели с полезными ссылками
    authentication_classes = [SessionAuthentication, TokenAuthentication]  # Авторизация по API будет ещё включать через токен
    permission_classes = [IsAdminUser | ReadOnly] # Доступ к изменению данных через API есть только у админа, для остальных лишь чтение
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer

class HistoryDataViewSet(viewsets.ModelViewSet): # Создаём ViewSet для модели с историческими датами НИИ со стандартным доступом в settings.py
    queryset = HistoryData.objects.all()
    serializer_class = HistoryDataSerializer

class HistoryViewSet(viewsets.ModelViewSet): # Создаём ViewSet для модели с историческими событиями НИИ со стандартным доступом в settings.py
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class CultureGroupViewSet(viewsets.ModelViewSet): # Создаём ViewSet для модели с группами культур НИИ
    authentication_classes = [SessionAuthentication, TokenAuthentication]  # Авторизация по API будет ещё включать через токен
    permission_classes = [IsAdminUser | ReadOnly] # Доступ к изменению данных через API есть только у админа, для остальных лишь чтение
    queryset = CultureGroup.objects.all()
    serializer_class = CultureGroupSerializer

class CultureViewSet(viewsets.ModelViewSet): # Создаём ViewSet для модели с возделываемыми культурами НИИ со стандартным доступом в settings.py
    queryset = Culture.objects.all()
    serializer_class = CultureSerializer

class TaxonViewSet(viewsets.ModelViewSet): # Создаём ViewSet для модели с возделываемыми таксонами НИИ со стандартным доступом в settings.py
    queryset = Taxon.objects.all()
    serializer_class = TaxonSerializer

class DocumentViewSet(viewsets.ModelViewSet): # Создаём ViewSet для модели с ксивами НИИ со стандартным доступом в settings.py
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class ProdCategoryViewSet(viewsets.ModelViewSet): # Создаём ViewSet для модели с категориями качества продукции НИИ со стандартным доступом в settings.py
    queryset = ProdCategory.objects.all()
    serializer_class = ProdCategorySerializer

class PriceViewSet(viewsets.ModelViewSet): # Создаём ViewSet для модели с прайс-листами НИИ со стандартным доступом в settings.py
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class NewsPictureViewSet(viewsets.ModelViewSet): # Создаём ViewSet для модели с изображениями для новостей НИИ со стандартным доступом в settings.py
    queryset = NewsPicture.objects.all()
    serializer_class = NewsPictureSerializer

class NewsViewSet(viewsets.ModelViewSet): # Создаём ViewSet для модели с новостями НИИ со стандартным доступом в settings.py
    queryset = News.objects.prefetch_related('img') # Для оптимизации количества запросов при связи многие-ко-многим (было 47, стало 3)
    serializer_class = NewsSerializer