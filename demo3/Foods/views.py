from django.shortcuts import render,redirect,reverse
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import *

# Create your views here.
def about(request):
    msg = Cook.objects.all()
    temp = Body.objects.all()
    return render(request,"about.html",locals())


def blog(request):
    return render(request,"blog.html")


def contact(request):
    if request.method == "POST":
        x = Subject()
        x.username = request.session["username"]
        x.email = request.POST.get("Email")
        x.sub = request.POST.get("Subject")
        x.detal = request.POST.get("Detail")
        x.save()
        return render(request, "contact.html", {"msg": "提交成功"})
    else:
        return render(request, "contact.html")
def gallery(request):
    return render(request,"gallery.html")


def menu(request):
    temp1 = Shop.objects.all().order_by("-num")[:4]
    temp2 = Shop.objects.all().order_by("-date")[:4]
    temp = Style.objects.all()
    # paginator = Paginator(temp, 1)
    #     # page = paginator.get_page(1)
    return render(request, "menu.html",locals())


def index(request):
    temp1 = Shop.objects.all().order_by("-num")[:4]
    temp2 = Shop.objects.all().order_by("-date")[:4]
    temp3 = Style.objects.all()
    msg = Body.objects.all()
    hero = Hero.objects.all()[1:3]
    log = Log.objects.dates(field_name="create_time", kind="month", order='DESC')

    return render(request, "index.html", locals())


def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(username,password)
        try:
            user = User.objects.get(username=username)
            # if user.username != username:
            #     return render(request, "register.html", {"msg": "用户名不存在，请注册"})
            if user.password != password:
                return render(request, "login.html", {"msg": "密码错误"})
            else:
                request.session["username"] = username
                res = redirect(reverse('food:index'))
                return res
            # return redirect(reverse('food:index'))
        except Exception as e:
            print("错误信息",e)
            return render(request, "login.html", {"msg": "用户名或密码错误,或未注册，请注册"})


def register(request):
    if request.method == "GET":
        return render(request,"register.html")
    else:
        username = request.POST.get("username").strip()
        password = request.POST.get("password").strip()
        password2 = request.POST.get("password2").strip()

        # 用户名不能为空
        if username == " " or username == None:
            return render(request, "register.html", {"msg": "用户名不能为空"})
        # 判断密码是否小于6位
        if len(password) < 6:
            return render(request, "register.html", {"msg": "密码不能小于6位，请重新输入"})
        # 判断密码是否一致
        if password != password2:
            return render(request, "register.html", {"msg": "两次密码不一致"})
        # 用户名是否存在
        user = User.objects.filter(username=username)
        if len(user) > 0:
            return render(request, "register.html", {"msg": "用户名已存在，请重新输入"})

        # 添加用户
        try:
            user = User(username=username, password=password)
            user.save()
            return redirect(reverse('food:login'))
        except Exception as e:
            print("添加出错，错误信息是：", e)
            return render(request, "register.html", {"msg": "注册失败，请重新注册"})



def single(request):
    return render(request,"single.html")


def logout(request):
    res = redirect(reverse('food:index'))
    request.session.flush()
    return res


def text(request):
    msg = "您尚未登录，请登录"
    return render(request, "login.html",{"msg": msg})


def error(request):
    return render(request,"404.html")
