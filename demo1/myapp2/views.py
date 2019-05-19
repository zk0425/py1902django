from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Article,List
from django.shortcuts import redirect
# Create your views here.


def index(request):
    return render(request, "myapp2/index.html", {"username": "赵奎"})
def list(request):
    return render(request, "myapp2/list.html")
def detail(request, id):
    return HttpResponse("<h1>这是一个详情第%s页面</h1>"%id)
def a1(request):
    # Article.objects.all()
    if request.method == "GET":
        return render(request, "myapp2/a1.html")
    elif request.method == "POST":
        value = request.POST["value"]
        num = List.objects.get("num")
        if value == "章":
            num +=1
            



def a1_1(request):
    if request.method == "POST":
        return render(request,"myapp2/a1_1.html")
def a2(request):
    return render(request,"myapp2/a2.html")
def a2_2(request):
    return render(request,"myapp2/a2_2.html")
def a3(request):
    return render(request,"myapp2/a3.html")
def a3_3(request):
    return render(request,"myapp2/a3_3.html")
def a4(request):
    return render(request,"myapp2/a4.html")
def a4_4(request):
    return render(request,"myapp2/a4_4.html")
def a5(request):
    return render(request,"myapp2/a5.html")
def a5_5(request):
    return render(request,"myapp2/a5_5.html")