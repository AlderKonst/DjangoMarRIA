from rest_framework import viewsets # Импортируем viewsets для создания представлений на основе моделей
from .models import * # Импортируем все модели из текущего приложения
from .serializers import * # И соответствующие сериализаторы

class TrendViewSet(viewsets.ModelViewSet): # Создаём ViewSet для модели
    queryset = Trend.objects.all() # Определяем queryset, который будет возвращать все объекты модели
    serializer_class = TrendSerializer # Указываем сериализатор, который будет использоваться для преобразования данных модели

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class TrendItemViewSet(viewsets.ModelViewSet):
    queryset = TrendItem.objects.all()
    serializer_class = TrendItemSerializer

class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer

class HistoryDataViewSet(viewsets.ModelViewSet):
    queryset = HistoryData.objects.all()
    serializer_class = HistoryDataSerializer

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class CultureGroupViewSet(viewsets.ModelViewSet):
    queryset = CultureGroup.objects.all()
    serializer_class = CultureGroupSerializer

class CultureViewSet(viewsets.ModelViewSet):
    queryset = Culture.objects.all()
    serializer_class = CultureSerializer

class TaxonViewSet(viewsets.ModelViewSet):
    queryset = Taxon.objects.all()
    serializer_class = TaxonSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class ProdCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProdCategory.objects.all()
    serializer_class = ProdCategorySerializer

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class NewsPictureViewSet(viewsets.ModelViewSet):
    queryset = NewsPicture.objects.all()
    serializer_class = NewsPictureSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer