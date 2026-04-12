from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Contact
from catalog.models import Product


def home(request):
    # получение 5 последних продуктов
    products = Product.objects.all()
    context = {"products": products}

    return render(request, "home.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
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
