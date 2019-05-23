from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.


class Tags(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "标签"
        verbose_name_plural = verbose_name

class Classify(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "分类"
        verbose_name_plural = verbose_name

class Article(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    reads = models.IntegerField(default=0)

    classify = models.ForeignKey(Classify, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)
    auth = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    class Meta():
        verbose_name = "文章"
        verbose_name_plural = verbose_name


# 富文本框

class MessageInfo(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=50)
    info = HTMLField()