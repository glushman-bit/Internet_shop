import os

from django.core.management.base import BaseCommand
from users.models import User
from dotenv import load_dotenv


load_dotenv()


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(email=os.getenv("ADMIN_EMAIL"))
        user.set_password(os.getenv("ADMIN_PASSWORD"))
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
