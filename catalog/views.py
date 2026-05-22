from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import View

from catalog.forms import ProductForm
from catalog.models import Category
from catalog.models import Contact
from catalog.models import Product

from .services import get_products_by_category_slug


@method_decorator(cache_page(60 * 5), name="dispatch")
class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "page_object"
    paginate_by = 6
    ordering = ["-id"]

    def get_queryset(self):
        return Product.objects.order_by("-published")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()

        return context


@method_decorator(cache_page(60 * 5), name="dispatch")
class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:product_list")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")
    permission_required = "catalog.can_add_product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or user.is_superuser:
            return ProductForm
        raise PermissionDenied


@method_decorator(cache_page(60 * 5), name="dispatch")
class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def test_func(self):
        product = self.get_object()
        user = self.request.user
        is_owner = user == product.owner
        is_moderator = user.is_superuser or user.groups.filter(name="Модератор продуктов").exists()

        cache.clear()

        return is_owner or is_moderator


class CategoryProductsListView(ListView):
    template_name = "catalog/product_category_list.html"
    context_object_name = "products"
    paginate_by = 6

    def get_queryset(self):
        # Захватываем slug из URL-адреса
        category_slug = self.kwargs.get("category_slug")
        self.category, products = get_products_by_category_slug(category_slug)
        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = self.category
        # Добавляем все категории для вывода в боковое меню
        context["all_categories"] = Category.objects.all()
        return context


class ContactListView(ListView):
    model = Contact
    template_name = "catalog/contacts.html"
    context_object_name = "contacts"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        print(f"name: {name},\n" f"phone: {phone},\n" f"message: {message}")

        return HttpResponse(f"Привет {name}, ваши данные приняты.")


class ProductUnpublishView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden("У вас не доступа для снятия продукта с публикации.")

        product.published = False
        product.save()

        return redirect("catalog:product_list")
