from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Добавление продуктов в базу данных из фикстуры'

    def handle(self, *args, **kwargs):
        """ Удаление существующих записей. """

        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'catalog/fixtures/catalog_fixture.json')
        self.stdout.write(self.style.SUCCESS('Данные успешно загружены из фикстуры.'))
