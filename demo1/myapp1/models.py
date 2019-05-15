from django.db import models


class Bookinfo(models.Model):
    bookname = models.CharField(max_length=30, verbose_name='书名')
    autor = models.CharField(max_length=30, verbose_name='作者')
    postedtime = models.DateField(auto_now_add=True, verbose_name='发表时间')
    altertime = models.DateField(auto_now=True, verbose_name='修改时间')


def __str__(self):
    return self.bookname


class Heroinfo(models.Model):
    name = models.CharField(max_length=30, verbose_name='名字')
    gender = models.CharField(max_length=10, choices=((0, "男"), (1, "女")), verbose_name='性别')
    book = models.ForeignKey(Bookinfo, on_delete=models.CASCADE, verbose_name='书名')


def __str__(self):
    return self.name
