from django.db import models
import datetime
from datetime import timezone
from django.utils import timezone


class Article(models.Model):
    Article_title = models.CharField('Название статьи', max_length=255)
    Article_text = models.TextField('Текст статьи')
    Article_publication = models.DateTimeField('Дата и время публикации', default=datetime.datetime.now())

    def __str__(self):
        return self.Article_title

    def was_published_recently(self):  # Получается, что к этим функциям класса Article можно обращаться отдельно от любого экземпляра класса Article. Сделал это в detail.html, когда указывал на то, что статья новая
        return self.Article_publication >= (timezone.now() - datetime.timedelta(days=3))

    class Meta:
        verbose_name = 'Article (verbose, single)'
        verbose_name_plural = 'Articles (verbose, plural)'


class Comment(models.Model):
    Comment_Article_FK = models.ForeignKey(Article, on_delete=models.CASCADE)
    Comment_author = models.CharField('Автор комментария', max_length=255)
    Comment_text = models.CharField('Текст комментария', max_length=500)

    def __str__(self):
        return self.Comment_author

    class Meta:
        verbose_name = 'Comment (verbose, single)'
        verbose_name_plural = 'Comments (verbose, plural)'