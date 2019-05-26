from django.shortcuts import render, redirect,reverse,get_list_or_404,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.views.generic import View
from django.core.mail import send_mail,send_mass_mail,EmailMultiAlternatives
from django.conf import settings
# 序列化加密
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from PIL import Image,ImageDraw,ImageFont
import random,io
from .models import Poll, User
from .util import checklogin
# Create your views here.
# class Login(View):
#     def get(self,request):
#         return render(request,"myapp2/login.html")
#     def post(self,request):
#         username = request.POST.get("username")
#         if username == "赵奎":
#             # return HttpResponse("登录成功")
#             # return redirect("/myapp2/index/")
#             return HttpResponseRedirect("/myapp2/index/")
#         else:
#             return render(request, "myapp2/login.html", {"error": "用户名错误"})
def login(request):
    if request.method == "GET":
        return render(request, "myapp2/login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        verfifycode = request.POST.get("verfify")
        print(username,verfifycode)
        # 验证码验证
        if verfifycode == request.session.get("verfifycode"):
            return render(request, "myapp2/login.html", {"error": "验证码错误"})
        else:
            # 邮箱验证登录
            user= get_object_or_404(User,username=username)
            if not user.is_active:
                return render(request, "myapp2/login.html", {"error": "用户尚未激活"})
            else:
                check =user.check_password(password)
                if check:
                    try:
                        user = User.objects.get(username=username)
                        if user.password != password:
                            return render(request, "myapp2/login.html", {"error": "密码错误"})
                        else:
                            # # return HttpResponse("登录成功")
                            # res=render(request,'myapp2/index.html',locals())
                            # # res = redirect("/myapp2/index/")
                            # # 设置cookie 完成登录
                            # # res.set_cookie("username", username)
                            request.session["username"] = username
                            res = redirect(reverse('roos:index'))
                            # return HttpResponseRedirect('/myapp2/index/')
                            # return redirect(reverse('roos:index'))
                            return res
                    except Exception as e:
                        print(e)
                        return render(request, "myapp2/login.html", {"error": "用户名或密码错误"})

def register(request):
    if request.method == "GET":
        return render(request, "myapp2/register.html")
    else:
        # print("+++++++++++++++++++++++++++++++++++")

        username = request.POST["username"].strip()
        password = request.POST["password"].strip()
        password2 = request.POST["password2"].strip()

        # 用户名不能为空
        if username == " "or username == None:
            return render(request, "myapp2/login.html", {"error": "用户名不能为空"})
        # 判断密码是否小于6位
        if len(password) < 6:
            return render(request, "myapp2/login.html", {"error": "密码不能小于6位，请重新输入"})
        # 判断密码是否一致
        if password != password2:
            return render(request, "myapp2/login.html", {"error": "两次密码不一致"})
        # 用户名是否存在
        user = User.objects.filter(username=username)
        if len(user) > 0:
            return render(request, "myapp2/login.html", {"error": "用户名已存在，请重新输入"})

        # 添加用户
        try:
            user = User(username=username, password=password)
            user.save()
            # 邮件验证
            user = User.objects.create_user(username=username,password=password, url='http://zzy0371.com')
            print(user.id,user.username,user.is_active)
            # 注册用户设置默认为非激活状态
            user.is_active = False
            user.save()
            # send mail 的使用
            # url = '<a href=+"http:192.168.14.146:8080/myapp2/active/%s/"%(user.id)>点击激活</a>'
            # send_mail("点击激活用户",url,settings.DEFAULT_FROM_EMAIL,['1098325439@qq.com'])

            # 将激活地址加密
            # 1.得到序列化工具  expires_in为有效期时间  默认为3600
            serutil = Serializer(settings.SECRET_KEY,expires_in=1000)
            # 2.使用序列化工具对字典进行序列化
            result = serutil.dumps({"userid":user.id}).decode("utf-8")



            # EmailMultiAlternatives 的使用
            mail = EmailMultiAlternatives("点击激活用户",'<a href=+"http:192.168.14.146:8080/myapp2/active/%s/">点击激活</a>'%(result,),settings.DEFAULT_FROM_EMAIL,['1098325439@qq.com'])
            mail.content_subtype = "html"
            mail.send()

            # return render(request, "myapp2/login.html", {"error": "注册成功"})
            return redirect(reverse("roos:login"))
        except Exception as e:
            print("添加出错，错误信息是：", e)
            return render(request, "myapp2/login.html", {"error": "注册失败，请重新注册"})

        # user = User()
        # user.username = username
        # user.password = password
        # user.save()

        # temp = User.objects.filter(username=username)
        # if len(temp) == 0:
        #     if username != " ":
        #         if password != " "and password == password2:
        #               user.save()
        #               return redirect(reverse("roos:login"))
        #         else:
        #             return render(request, "myapp2/register.html", {"error": "密码错误"})
        #     else:
        #         return render(request, "myapp2/register.html", {"error": "用户名错误"})
        # else:
        #     return render(request, "myapp2/register.html", {"error": "该用户已注册"})


def active(request,info):
    serutil = Serializer(settings.SECRET_KEY, expires_in=1000)
    try:
        obj = serutil.loads(info)
        print(obj["userid"])
        id = obj["userid"]
        user = get_object_or_404(User,pk=id)
        user.is_active = True
        user.save()
        return redirect(reverse("roos:login"))
    except Exception as e:
        print("错误信息是", e)
        return HttpResponse("过期了")


def verfify(request):
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    heigth = 25
    # 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, heigth))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    print(rand_str)
    # 构造字体对象
    # font = ImageFont.truetype('SCRIPTBL.TTF', 23)
    # fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    # draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    # draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    # draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    # draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    draw.text((5, 2), rand_str[0],)
    draw.text((25, 2), rand_str[1],)
    draw.text((50, 2), rand_str[2],)
    draw.text((75, 2), rand_str[3],)
    # 释放画笔
    del draw
    request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), '/img/png')


def logout(request):
    res = redirect(reverse('roos:login'))
    # res.delete_cookie("username")
    request.session.flush()
    return res
# class Index(View):
#     def get(self, request):
#         poll = Poll.objects.all()
#         return render(request, "myapp2/index.html", {"poll": poll})


@checklogin
def index(request): # 首页
        username = request.session["username"]
        # username = request.session.get("username")
        poll = Poll.objects.all()
        return render(request, "myapp2/index.html", locals())


@checklogin
def list(request,id): # 选择页
    # poll = Poll.objects.get(pk=id)
    poll = get_object_or_404(Poll, pk=id)
    # poll = get_list_or_404(Poll, pk__gt=id)
    if request.method == "GET":
        return render(request, "myapp2/list.html", {"poll": poll})
    else:
        value = request.POST['sex']
        if value == "1":
            poll.name_one_num += 1
        else:
            poll.name_two_num += 1
        poll.save()
        # return redirect("/myapp2/detail/%s/" % (poll.id,))
        # 使用reverse解除硬编码，又称反向解析
        return redirect(reverse('roos:detail', args=(id,)))

@checklogin
def detail(request, id): # 详情信息页
    # return HttpResponse('ok')
    poll = Poll.objects.get(pk=id)
    return render(request, 'myapp2/detail.html', {'poll': poll})

