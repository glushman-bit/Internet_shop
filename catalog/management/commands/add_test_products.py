from django.core.management.base import BaseCommand

from catalog.models import Category
from catalog.models import Product


class Command(BaseCommand):
    help = 'Добавление продуктов в базу данных'

    def handle(self, *args, **kwargs):
        """ Удаление существующих записей. """

        category, _ = Category.objects.get_or_create(name='Бытовая техника', description='Техника для жизни.')

        products = [
            {"name": "Gefest",
             "description": "Лучшее для дома",
             "category": category,
             "price": "42000.00",
             },
            {"name": "Indezit",
             "description": "Качество по доступной цене",
             "category": category,
             "price": "18000.00",
             }
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Продукт успешно добавлен: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Продукт уже существует: {product.name}'))
