from django import template
from blog.models import Tags, Classify, Article, AddImg
register = template.Library()

"""
过滤器最多两个参数
标签可以有任意多个参数
"""
@register.filter(name='mylower')
def mylower(value):
    return value.lower()

@register.filter(name='myslice')
def myslice(value,length):
    result = value[:length]
    print(result)
    return  result


# 注册标签
@register.simple_tag()
def gettags():
    return Tags.objects.all()
# 注册最新文章
@register.simple_tag()
def getlatestarticles(num=3):
    return Article.objects.all().order_by("-create_time")[:num]
# 注册归档
@register.simple_tag()
def getarchives (num = 3):
    return Article.objects.dates("create_time","month",order="DESC")[:num]

# 注册分类
@register.simple_tag(name='getcategorys')
def getcategorys():
    return Classify.objects.all()

# 注册轮播图
@register.simple_tag()
def getaddimg():
    return AddImg.objects.all()