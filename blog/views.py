from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "blog/article_list.html"
    context_object_name = "page_object"
    paginate_by = 10
    ordering = ["-created_at"]

    def get_queryset(self):
        return Article.objects.order_by("is_active")


class ArticleDetailView(DetailView):
    model = Article
    template_name = "blog/article_detail.html"
    context_object_name = "article"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ArticleCreateView(CreateView):
    model = Article
    fields = ("title", "content", "image")
    template_name = "blog/article_form.html"
    success_url = reverse_lazy("blog:article_list")


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ("title", "content", "image")
    template_name = "blog/article_form.html"

    def get_success_url(self):
        return reverse_lazy("blog:article_detail", args=[self.kwargs["pk"]])


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "blog/article_confirm_delete.html"
    success_url = reverse_lazy("blog:article_list")