import os

from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "form-control",
                }
            )


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("created_at", "updated_at", "views_count",)
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name', '').lower()
        description = cleaned_data.get('description', '').lower()

        forbidden_words = [
            "казино",
            "биржа",
            "криптовалюта",
            "крипта",
            "дешево",
            "бесплатно",
            "обман",
            "полиция",
            "радар",
        ]
        for word in forbidden_words:
            if word in name or word in description:
                raise ValidationError(f"Слово '{word}' запрещено к использованию")

        return cleaned_data


    def clean_price(self):
        price = self.cleaned_data["price"]

        if price <= 0:
            raise ValidationError("Цена не может быть отрицательной или равной 0")
        return price

    def clean_image(self):
        image = self.cleaned_data["image"]
        if image is None:
            return image

        formated_image = [
            ".JPG",
            ".png",
        ]
        _, file_ext = os.path.splitext(image.name)

        if file_ext not in formated_image:
            raise ValidationError("Неверный формат файла")
        elif image.size > 5 * 1024 * 1024:
            raise ValidationError("Неверный размер файла")
        return image