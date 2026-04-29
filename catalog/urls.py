from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

# from catalog.views import product_list

app_name = CatalogConfig.name

urlpatterns = [
    # path("", product_list, name="product_list"),
    path("contacts/", contacts, name="contacts"),
    # path("product_detail/<int:pk>/", product_detail, name="product_detail"),
    # path("create_product/", create_product, name="create_product"),

    path("", ProductListView.as_view(), name="product_list"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("catalog/create/", ProductCreateView.as_view(), name="product_create"),
    path("catalog/<int:pk>/update/", ProductUpdateView.as_view(), name="product_create"),
    path("catalog/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]
