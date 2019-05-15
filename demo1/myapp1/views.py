from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Heroinfo,Bookinfo
# from django.shortcuts import redirect
# Create your views here.


def index(request):
    # return HttpResponse("这是一个首页面")
    temp = loader.get_template("myapp1/index.html")
    result = temp.render({"username": "赵奎"})
    return HttpResponse(result)

def reg(request):
    return HttpResponse("<h1>这是一个注册页面</h1>")


def list(request):
    allbook = Bookinfo.objects.all()

    temp = loader.get_template("myapp1/list.html")
    result = temp.render({"allbook": allbook})
    return HttpResponse(result)


def detail(request,id):
    book = None
    try:
        book = Bookinfo.objects.get(pk=id)
    except Exception as e:
        return HttpResponse("没有书籍信息")
    temp = loader.get_template("myapp1/detail.html")
    result = temp.render({"book": book})
    return HttpResponse(result)
    # return HttpResponse("<h1>这是一个详情第%s页面</h1>"%id)
