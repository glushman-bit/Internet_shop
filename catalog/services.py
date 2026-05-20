from django.shortcuts import get_object_or_404

from .models import Category
from .models import Product


def get_active_products_by_category(category_id: int):
    """ Возвращает список товаров, относящихся к заданной категории. """
    products = Product.objects.filter(category=category_id)
    return products


def get_category_name_by_id(category_id: int):
    """ Возвращает название категории, связанной с заданным id. """
    category = get_object_or_404(Category, id=category_id)
    return category.name
