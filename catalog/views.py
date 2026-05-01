from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Contact, Category
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "page_object"
    paginate_by = 6
    ordering = ["-id"]


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"
    success_url =reverse_lazy("catalog:product_list")


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        category_name = request.POST.get("category")
        price = request.POST.get("price")

        category, _ = Category.objects.get_or_create(name=category_name)

        product = Product(
            name=name,
            description=description,
            category=category,
            price=price
        )

        if image:
            product.image = image

        product.save()

        return redirect("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name", "description", "image", "category", "price"]
    template_name = "catalog/product_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_list"] = Category.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.name = request.POST.get("name")
        self.object.description = request.POST.get("description")

        if request.FILES.get("image"):
            self.object.image = request.FILES.get("image")

        category_id = request.POST.get("category")
        if category_id:
            category = get_object_or_404(Category, pk=category_id)
            self.object.category = category


        if request.POST.get("price"):
            self.object.price = request.POST.get("price")

        self.object.save()

        return redirect("catalog:product_detail", self.object.pk)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")



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
