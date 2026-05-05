from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleCreateView
from blog.views import ArticleDeleteView
from blog.views import ArticleDetailView
from blog.views import ArticleListView
from blog.views import ArticleUpdateView

app_name = BlogConfig.name

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("create/", ArticleCreateView.as_view(), name="article_create"),
    path("<int:pk>/update/", ArticleUpdateView.as_view(), name="article_create"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
]
