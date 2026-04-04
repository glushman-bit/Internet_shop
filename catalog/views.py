from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product, Contact


def home(request):
    # получение 5 последних продуктов
    latest_products = Product.objects.order_by("-created_at")[:5]

    # вывод продуктов в консоль
    print("Последние 5 продуктов.")
    for product in latest_products:
        print(product.name)


    return render(request, "home.html", {"latest_products": latest_products})


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

    # if request.method == "POST":
    #     name = request.POST.get("name")
    #     phone = request.POST.get("phone")
    #     message = request.POST.get("message")
    #     print(f"Имя : {name},\n" f"Телефон : {phone},\n" f"Сообщение : {message}")
    #
    #     return HttpResponse(f"Привет {name}, ваши данные приняты.")