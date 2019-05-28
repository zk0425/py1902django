from django.shortcuts import render,redirect,reverse
from .models import *

# Create your views here.
def about(request):
    return render(request,"about.html")


def blog(request):
    return render(request,"blog.html")


def contact(request):
    return render(request,"contact.html")


def gallery(request):
    return render(request,"gallery.html")


def index(request):
    temp = Body.objects.all()
    return render(request, "index.html", {"msg": temp})



def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.get(username=username)
        if user.password != password:
            return render(request, "myapp2/login.html", {"msg": "密码错误"})
        else:
            return redirect(reverse('food:index'))


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
