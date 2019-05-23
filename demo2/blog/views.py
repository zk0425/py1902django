from django.shortcuts import render,get_object_or_404,redirect
from .models import Article,Classify,Tags
from django.http import HttpResponse,HttpResponseRedirect
# 分页
from django.core.paginator import Paginator
from comments.forms import DiscussForm
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

def contact(request):
    return render(request,'contact.html')