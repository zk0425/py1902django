from django.db import models
from blog.models import Article
# Create your models here.


class Discuss(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    urls = models.CharField(max_length=50)
    comment = models.TextField(max_length=500)
    comments = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
    class Meta():
        verbose_name = "评论"
        verbose_name_plural = verbose_name
