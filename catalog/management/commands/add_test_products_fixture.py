from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category
from catalog.models import Product


class Command(BaseCommand):
    help = 'Добавление продуктов в базу данных из фикстуры'

    def handle(self, *args, **kwargs):
        """ Удаление существующих записей. """

        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'catalog/fixtures/catalog_fixture.json')
        self.stdout.write(self.style.SUCCESS('Данные успешно загружены из фикстуры.'))
