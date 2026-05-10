from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название продукта", help_text="Введите название продукта")
    description = models.TextField(
        verbose_name="Описание продукта", help_text="Введите описание продукта", blank=True, null=True
    )
    image = models.ImageField(
        upload_to="products/photos",
        blank=True,
        null=True,
        verbose_name="Фото продукта",
        help_text="Загрузка фото продукта",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="products",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена продукта")
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания продукта",
    )
    updated_at = models.DateField(
        auto_now=True,
        verbose_name="Дата изменения продукта",
    )
    views_count = models.IntegerField(
        default=0,
        verbose_name="Счетчик просмотров",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    description = models.TextField(
        verbose_name="Описание категории", help_text="Введите описание категории", blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес",
        blank=True,
        null=True,
    )
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Электронная почта")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
