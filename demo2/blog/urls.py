from django.conf.urls import url
from . import views
from . import feed
app_name = "blog"
urlpatterns = [
    url(r'^rss/$', feed.BlogFeed(), name='rss'),
    url(r'^single/(\d+)/$', views.single, name="single"),
    url(r'^category/(\d+)/$', views.category, name="category"),
    url(r'^archives/(\d+)/(\d+)/$', views.archives, name="archives"),
    url(r'^tag/(\d+)/$', views.tag, name="tag"),
    url(r'^contactus/$', views.contactus, name="contactus"),
    url(r'^addimg/$', views.addimg, name="addimg"),
    url(r'', views.index, name="index"),

]