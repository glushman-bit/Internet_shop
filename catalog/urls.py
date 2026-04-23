from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, product_detail, create_product
from catalog.views import product_list

app_name = CatalogConfig.name

urlpatterns = [
    path("", product_list, name="product_list"),
    path("contacts/", contacts, name="contacts"),
    path("product_detail/<int:pk>/", product_detail, name="product_detail"),
    path("create_product/", create_product, name="create_product"),
]
