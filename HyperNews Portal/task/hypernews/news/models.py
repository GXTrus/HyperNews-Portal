import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

# News post
class NewsPost(models.Model):
    post_title = models.CharField('название статьи', max_length=200)  # News title
    post_text = models.TextField('текст статьи')  # News text
    post_datetime = models.DateTimeField('дата публикации')  # News date
    post_id = models.IntegerField('id и ссылка статьи')  # News ID

    def __str__(self):
        return f'{self.post_title}:\n{self.post_datetime}\n {self.post_text}'

    def published_in_days(self, n_days):
        return self.post_datetime >= (timezone.now() - datetime.timedelta(days=n_days))

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

# Post's comment
class PostComment(models.Model):
    post = models.ForeignKey(NewsPost, on_delete=models.CASCADE)
    comment_author = models.CharField('автор комментария', max_length=50)  # Comment's author
    comment_text = models.CharField('текст статьи', max_length=200)  # Text of comment

    def __str__(self):
        return f'{self.comment_author}: {self.comment_text}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
