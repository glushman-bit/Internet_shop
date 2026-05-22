from django.contrib.auth.forms import UserCreationForm

from catalog.forms import StyleFormMixin

from .models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "phone_number", "avatar", "country", "password1", "password2")
