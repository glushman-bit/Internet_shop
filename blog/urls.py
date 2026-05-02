from django.urls import path

from blog.apps import BlogConfig
from blog.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("create/", ArticleCreateView.as_view(), name="article_create"),
    path("<int:pk>/update/", ArticleUpdateView.as_view(), name="article_create"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
]
