from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactListView
from catalog.views import ProductCreateView
from catalog.views import ProductDeleteView
from catalog.views import ProductDetailView
from catalog.views import ProductListView
from catalog.views import ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name="product_create"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("contacts/", ContactListView.as_view(), name="contacts"),
]
