from django.db import models

# Create your models here.


class Poll(models.Model):
    title = models.CharField(max_length=20, )
    name_one = models.CharField(max_length=20,)
    name_two = models.CharField(max_length=20,)
    name_one_num = models.IntegerField(default=0)
    name_two_num = models.IntegerField(default=0)


class User(models.Model):
    username = models.CharField(max_length=20,null=False,)
    password = models.CharField(max_length=20)
