from django.db import models
from pytils.translit import slugify

from config import settings


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
    published = models.BooleanField(null=True, blank=True, default=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Владелец",
        on_delete=models.CASCADE,
        help_text="Укажите владельца продукта",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    description = models.TextField(
        verbose_name="Описание категории", help_text="Введите описание категории", blank=True, null=True
    )
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL-слаг")

    def save(self, *args, **kwargs):
        """Генерация slug из имени категории"""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_absolute_url(self):
        """Метод генерации ссылок на категорию"""
        return reverse("category_product", kwargs={"category_slug": self.slug})


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
