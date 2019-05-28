from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
# 发送邮件
from django.core.mail import send_mail,send_mass_mail
# 分页
from django.core.paginator import Paginator
from django.views.generic import View
# 导入setting文件
from django.conf import settings
from jieba.analyse import ChineseAnalyzer
from comments.forms import DiscussForm
from .models import Article,Classify,Tags,MessageInfo,AddImg

# import markdown

# Create your views here.


def index(request):
    pagenum=request.GET.get("page")
    pagenum = 1 if pagenum==None else pagenum
    articles = Article.objects.all().order_by("-reads")
    paginator = Paginator(articles, 1)
    page=paginator.get_page(pagenum)



    return render(request, "index.html", {"page":page})

def single(request, id):
    article = get_object_or_404(Article, pk=id)

    article.reads += 1
    article.save()
    # article.body = markdown.markdown(article.body, extensions=[
    #     'markdown.extensions.extra'
    #     'markdown.extensions.codehilite'
    #     # 'markdown.extensions.toc'
    # ])


    df = DiscussForm()
    return render(request, "single.html", locals())

def tag(request,id):
    articles = get_object_or_404(Tags, pk=id).article_set.all()
    paginator = Paginator(articles,1)
    page = paginator.get_page(1)

    return render(request, 'index.html', {"page": page})

def archives(request,year,month):
    articles = Article.objects.filter(create_time__year=year, create_time__month=month)
    paginator = Paginator(articles,1)
    page = paginator.get_page(1)
    return render(request,'index.html', {"page":page})
def category(request,id):
    articles =get_object_or_404(Classify,pk=id).article_set.all()
    paginator = Paginator(articles, 1)
    page = paginator.get_page(1)
    return render(request,'index.html',{"page":page})


def contactus(request):
    if request.method == "GET":
        return render(request, 'contact.html')
    elif request.method == "POST":
        try:
            # 发一封邮件
            send_mail("测试文件","这是一封文件",settings.DEFAULT_FROM_EMAIL,["1098325439@qq.com"])
            # 发多封邮件
            send_mass_mail((("测试文件1","这是第一封文件",settings.DEFAULT_FROM_EMAIL,["1098325439@qq.com"]),
                            ("测试文件2", "这是第二封文件", settings.DEFAULT_FROM_EMAIL, ["1098325439@qq.com"]),
                            ("测试文件3", "这是第三封文件", settings.DEFAULT_FROM_EMAIL, ["1098325439@qq.com"])
                           ))
        except Exception as e:
            print("错误信息",e)


        x = MessageInfo()
        x.username = request.POST.get("name")
        x.email = request.POST.get("email")
        x.subject = request.POST.get("subject")
        x.info = request.POST.get("message")
        x.save()
        return render(request, 'contact.html')



def addimg(request):
    if request.method == 'GET':
        return render(request, 'addimg.html')
    else:
        img = request.FILES.get("img")
        desc = request.POST.get("desc")
        x = AddImg(img=img,desc=desc)
        x.save()
        # imglist = AddImg.objects.all()
        return render(request, "addimg")
