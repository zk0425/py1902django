from django.shortcuts import render,get_object_or_404
from .models import Article
# 分页
from django.core.paginator import Paginator
import markdown

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
    return render(request, "single.html", locals())
