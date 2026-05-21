from django.core.cache import cache
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Category
from .models import Product


def get_category_id_by_slug(category_slug: str) -> int:
    """Возвращает ID категории по её slug через кэш."""
    slug_cache_key = f"category_slug_{category_slug}"
    category_id = cache.get(slug_cache_key)

    if not category_id:
        category_id = Category.objects.filter(slug=category_slug).values_list("id", flat=True).first()
        if not category_id:
            raise Http404("Категория не найдена")

        cache.set(slug_cache_key, category_id, timeout=60 * 60 * 24)

    return category_id


def get_category_with_cache(category_id: int):
    """ Функция кэширования объекта категории по ID."""
    cache_key = f"category_{category_id}"
    category = cache.get(cache_key)

    if not category:
        try:
            category = Category.objects.get(id=category_id)
            cache.set(cache_key, category, timeout=3600)  # TTL = 1 час
        except Category.DoesNotExist:
            return None
    return category


def get_products_by_category_slug(category_slug: str):
    """ Функция извлечения кэша из Redis. """
    category_id = get_category_id_by_slug(category_slug)
    category = get_category_with_cache(category_id)

    if not category:
        raise Http404("Категория не найдена")

    products = Product.objects.filter(category=category)
    return category, products
