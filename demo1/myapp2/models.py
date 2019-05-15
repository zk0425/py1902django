from django.db import models

# Create your models here.


from datetime import datetime
from django.db import models

# 管理器方法
# class UserManager(models.Manager):
#     def add_user(self, username, password):
#         user = self.create(username=username, password=password)
#         return user


class User(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='用户主键')
    username = models.CharField(max_length=50, verbose_name="用户名称", unique=True)
    password = models.CharField(max_length=50, verbose_name="用户密码")
    gender = models.CharField(max_length=10, default='男', verbose_name="用户性别")
    age = models.IntegerField(default=18, verbose_name="用户年龄")
    birthday = models.DateTimeField(default=datetime.now())

    # 管理器
    # userManager = UserManager()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.username
    # @classmethod
    # def create_user(cls, username, password):
    #     user = cls(username=username, password=password)
    #     return user


class Article(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="文章主题")
    title = models.CharField(max_length=200, verbose_name="文章标题")
    content = models.TextField(verbose_name="文章内容")
    publishTime = models.DateTimeField(auto_now_add=True)
    modifyTime = models.DateTimeField(auto_created=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
