from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Heroinfo,Bookinfo
from django.shortcuts import redirect
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

    # temp = loader.get_template("myapp1/list.html")
    # result = temp.render({"allbook": allbook})
    # return HttpResponse(result)

    return render(request, "myapp1/list.html", {"allbook": allbook})


def detail(request,id):
    # return HttpResponse("<h1>这是一个详情第%s页面</h1>"%id)
    book = None
    try:
        book = Bookinfo.objects.get(pk=id)
    except Exception as e:
        return HttpResponse("没有书籍信息")
    temp = loader.get_template("myapp1/detail.html")
    result = temp.render({"book": book})
    return HttpResponse(result)


def deletebook(request,id):
    Bookinfo.objects.get(pk=id).delete()
    return redirect('/myapp1/list/')


def deletehero(request,id):
    # Heroinfo.objects.get(pk=id).delete()
    hero = Heroinfo.objects.get(pk=id)
    bookid = hero.book.id
    hero.delete()
    return redirect('/myapp1/detail/%s'%(bookid,))


def addbook(request):
    pass


def addhero(request, id):
    if request.method == "GET":
        return render(request, 'myapp1/addhero.html', {"bookid":id})
    elif request.method == "POST":
        book = Bookinfo.objects.get(pk=id)
        hero = Heroinfo()
        hero.name = request.POST['username']
        hero.gender = request.POST['sex']
        hero.book = book
        hero.save()
        return redirect('/myapp1/detail/%s'% (id,))


def updatehero(request,id):
    if request.method == "GET":
        return render(request, 'myapp1/addhero.html', {"bookid":id})
    elif request.method == "POST":
        book = Bookinfo.objects.get(pk=id)
        hero = Heroinfo()
        hero.name = request.POST['username']
        hero.gender = request.POST['sex']
        hero.book = book
        hero.save()
        return redirect('/myapp1/detail/%s'% (id,))
