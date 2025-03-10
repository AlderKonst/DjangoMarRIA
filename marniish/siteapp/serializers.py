from rest_framework import serializers # Загружаем метод работы с сериализаторами
from .models import * # Импортируем все модели

class TrendSerializer(serializers.HyperlinkedModelSerializer): # Создаём сериализатор для модели
    class Meta:
        model = Trend # Указываем модель
        fields = '__all__' # Выбираем все поля модели

class ArticleSerializer(serializers.HyperlinkedModelSerializer): # Создаём сериализатор для модели
    class Meta:
        model = Article # Указываем модель
        fields = '__all__' # Выбираем все поля модели

class ProgressSerializer(serializers.HyperlinkedModelSerializer): # Создаём сериализатор для модели
    class Meta:
        model = Progress # Указываем модель
        fields = '__all__' # Выбираем все поля модели

class PageSerializer(serializers.HyperlinkedModelSerializer): # Создаём сериализатор для модели
    class Meta:
        model = Page # Указываем модель
        fields = '__all__' # Выбираем все поля модели

class TrendItemSerializer(serializers.HyperlinkedModelSerializer): # Создаём сериализатор для модели
    class Meta:
        model = TrendItem # Указываем модель
        fields = '__all__' # Выбираем все поля модели

class ReferenceSerializer(serializers.HyperlinkedModelSerializer): # Создаём сериализатор для модели
    class Meta:
        model = Reference # Указываем модель
        fields = '__all__' # Выбираем все поля модели

class HistoryDataSerializer(serializers.HyperlinkedModelSerializer): # Создаём сериализатор для модели
    class Meta:
        model = HistoryData # Указываем модель
        fields = '__all__' # Выбираем все поля модели

class HistorySerializer(serializers.HyperlinkedModelSerializer): # Создаём сериализатор для модели
    class Meta:
        model = History # Указываем модель
        fields = '__all__' # Выбираем все поля модели

class CultureGroupSerializer(serializers.HyperlinkedModelSerializer): # Создаём сериализатор для модели
    class Meta:
        model = CultureGroup # Указываем модель
        fields = '__all__' # Выбираем все поля модели

class CultureSerializer(serializers.HyperlinkedModelSerializer): # Создаём сериализатор для модели
    class Meta:
        model = Culture # Указываем модель
        fields = '__all__' # Выбираем все поля модели

class TaxonSerializer(serializers.HyperlinkedModelSerializer): # Создаём сериализатор для модели
    class Meta:
        model = Taxon # Указываем модель
        fields = '__all__' # Выбираем все поля модели

class DocumentSerializer(serializers.HyperlinkedModelSerializer): # Создаём сериализатор для модели
    class Meta:
        model = Document # Указываем модель
        fields = '__all__' # Выбираем все поля модели

class ProdCategorySerializer(serializers.HyperlinkedModelSerializer): # Создаём сериализатор для модели
    class Meta:
        model = ProdCategory # Указываем модель
        fields = '__all__' # Выбираем все поля модели

class PriceSerializer(serializers.HyperlinkedModelSerializer): # Создаём сериализатор для модели
    class Meta:
        model = Price # Указываем модель
        fields = '__all__' # Выбираем все поля модели

class NewsPictureSerializer(serializers.HyperlinkedModelSerializer): # Создаём сериализатор для модели
    class Meta:
        model = NewsPicture # Указываем модель
        fields = '__all__' # Выбираем все поля модели

class NewsSerializer(serializers.HyperlinkedModelSerializer): # Создаём сериализатор для модели
    class Meta:
        model = News # Указываем модель
        fields = '__all__' # Выбираем все поля модели