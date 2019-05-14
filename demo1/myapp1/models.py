from django.db import models


class Bookinfo(models.Model):
    bookname = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)
    postedtime = models.DateField(auto_now_add=True)
    altertime = models.DateField(auto_now=True)


def __str__(self):
    return self.bookname


class Heroinfo(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, default="男")
    book = models.ForeignKey(Bookinfo, on_delete=models.CASCADE)


def __str__(self):
    return self.name
