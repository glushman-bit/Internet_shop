from django.contrib import admin

from catalog.models import Category
from catalog.models import Contact
from catalog.models import Product


@admin.register(Product)
class CatalogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
        "category",
    )
    list_filter = ("category",)
    search_fields = (
        "name",
        "description",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "phone",
        "email",
    )
    list_filter = (
        "name",
        "phone",
    )
    search_fields = (
        "name",
        "phone",
    )
