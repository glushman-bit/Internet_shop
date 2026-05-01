from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название статьи",
    )
    content = models.TextField(
        max_length=1000,
        verbose_name="Тело контента",
    )
    image = models.ImageField(
        upload_to="blog/images",
        blank=True,
        null=True,
        verbose_name="Фото публикации",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время публикации",
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name="Статус публикации",
    )
    views_count = models.IntegerField(
        default=0,
        verbose_name="Счетчик просмотров",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["created_at"]