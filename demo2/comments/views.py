from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.views.generic import View
from django.http import HttpResponse,HttpResponseRedirect
from .models import Discuss
from blog.models import Article
from .forms import DiscussForm

# Create your views here.

class AddDiscuss(View):
    def post(self, request, id):
        article = get_object_or_404(Article, pk=id)
        df = DiscussForm(request.POST)
        if df.is_valid():
            username = df.cleaned_data["name"]
            email = df.cleaned_data["email"]
            url = df.cleaned_data["url"]
            comment = df.cleaned_data["comment"]

            d = Discuss()
            d.username = username
            d.email = email
            d.url = url
            d.content = comment
            d.article = article
            d.save()
            return redirect(reverse('blog:single', args=(id,)))
            # return HttpResponseRedirect('single/%s'%(id,))
            # return HttpResponse("success+++++++++++++++++++++++++++++++++")
        else:
            return HttpResponse("输入不合法")
