from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateView
from users.views import UserDetailView
from users.views import UserUpdateView
from users.views import email_verification

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="catalog:product_list"), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email_confirm"),
    path("profile/", UserDetailView.as_view(), name="profile"),
    path("profile/update/", UserUpdateView.as_view(), name="profile_update"),
]
