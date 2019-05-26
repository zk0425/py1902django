from django.contrib.syndication.views import Feed
from .models import Article
from django.shortcuts import reverse


class BlogFeed(Feed):
    title = "赵奎的个人博客"
    description = "一个优秀地博客网站"
    link = "/"

    def items(self):
        return Article.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body[:30]

    def item_link(self, item):
        return reverse('blog:single', args=(item.id,))
