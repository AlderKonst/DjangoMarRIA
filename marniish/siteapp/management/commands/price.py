from django.core.management.base import BaseCommand # Импорт базового класса команды Django
from siteapp.models import ProdCategory, Price # Импорт моделей из siteapp

# Здесь будет добавление данных в БД для страницы Price.html

class Command(BaseCommand):
    def handle(self, *args, **options):
        names = ['Суперсуперэлита', 'Суперэлита', 'Элита', 'Репродукция I', 'Репродукция II', 'Репродукция III']

        category, _ = ProdCategory.objects.get_or_create(name=name) #
        Price.objects.get_or_create( #
            taxon=taxon, #
            category=category, #
            mass=mass, #
            price=price) #