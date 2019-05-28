from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20, null=False,)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

    class Meta():
        verbose_name = "用户"
        verbose_name_plural = verbose_name


class Title(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "标题"
        verbose_name_plural = verbose_name


class Body(models.Model):
    title = models.CharField(max_length=20)
    littletitle = models.CharField(max_length=20)
    body = models.CharField(max_length=200,null=True)
    littlebody = models.CharField(max_length=100,null=True)
    img = models.ImageField()
    price = models.IntegerField(default=0,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    fo_id = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "内容"
        verbose_name_plural = verbose_name


class People(models.Model):
    name = models.CharField(max_length=20)
    skill = models.CharField(max_length=50)
    jianjie = models.CharField(max_length=200)
    fo_id = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "人物"
        verbose_name_plural = verbose_name


class AddImg(models.Model):
    img = models.ImageField(upload_to="imgs")
    desc = models.CharField(max_length=20)

    def __str__(self):
        return self.desc

    class Meta():
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name
