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


class Subject(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    sub = models.CharField(max_length=50)
    detal = models.CharField(max_length=500)

    def __str__(self):
        return self.username

    class Meta():
        verbose_name = "建议"
        verbose_name_plural = verbose_name


class Shop(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    img = models.ImageField()
    num = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True,verbose_name="时间")

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "商品"
        verbose_name_plural = verbose_name


class Style(models.Model):
    img = models.ImageField()
    name = models.CharField(default=" ", max_length=10)
    body = models.CharField(default=" ", max_length=50)

    def __str__(self):
        return self.img

    class Meta():
        verbose_name = "样式"
        verbose_name_plural = verbose_name


class Cook(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=500)
    img = models.ImageField()
    contact = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "厨师"
        verbose_name_plural = verbose_name


class Hero(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=500)
    img = models.ImageField()

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "荣誉"
        verbose_name_plural = verbose_name


class Log(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    place = models.CharField(max_length=50)
    deeds = models.CharField(max_length=200)
    img = models.ImageField()
    img2 = models.CharField(max_length=20)

    def __str__(self):
        return self.place

    class Meta():
        verbose_name = "记录"
        verbose_name_plural = verbose_name
