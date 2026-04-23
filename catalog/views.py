import datetime

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from catalog.models import Contact, Category
from catalog.models import Product


def product_list(request):
    products = Product.objects.all().order_by('-id')

    paginator = Paginator(products, 6)
    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)

    context = {"page_object": page_object}

    return render(request, "product_list.html", context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Имя : {name},\n" f"Телефон : {phone},\n" f"Сообщение : {message}")

        return HttpResponse(f"Привет {name}, ваши данные приняты.")

    contact_list = Contact.objects.all()
    print("Количество контактов: ", contact_list.count())

    for contact in contact_list:
        print(contact.name)

    return render(request, "contacts.html", {"contacts": contact_list})


def create_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        category = request.POST.get("category")
        price = request.POST.get("price")

        category, _ = Category.objects.get_or_create(name=category)

        product = Product.objects.create(
            name=name,
            description=description,
            image=image,
            category=category,
            price=price,
        )

        return redirect("catalog:product_detail", pk=product.pk)

    return render(request, "create_product.html")
