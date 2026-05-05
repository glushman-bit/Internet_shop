import os

from django.forms import ModelForm
from django import forms
from catalog.models import Product
from django.core.exceptions import ValidationError


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
            })


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        name_lower = name.lower()
        forbidden_words = [
            'казино', 'биржа', 'криптовалюта', 'крипта', 'дешево',
            'бесплатно', 'обман', 'полиция', 'радар',
        ]
        if name_lower in forbidden_words:
            raise ValidationError('это слово запрещено')
        return name

    def clean_price(self):
        price = self.cleaned_data['price']

        if price <= 0:
            raise ValidationError('Цена не может быть отрицательной или равной 0')
        return price

    def clean_image(self):
        image = self.cleaned_data['image']
        if image is None:
            return image

        formated_image = ['.jpg', '.png', ]
        _, file_ext = os.path.splitext(image.name)

        if file_ext not in formated_image:
            raise ValidationError('Неверный формат файла')
        elif image.size > 5 * 1024 * 1024:
            raise ValidationError('Неверный размер файла')
        return image
