from django.conf.urls import url
from . import views
app_name = "blog"
urlpatterns = [

    url(r'^single/(\d+)/$', views.single, name="single"),
    url(r'', views.index, name="index"),
]