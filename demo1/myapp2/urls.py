from django.conf.urls import url
from . import views
app_name = "roos"
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    # url(r'^index/$', views.Index.as_view(), name='index'),
    # url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^login/$', views.login, name='login'),
    url(r'^list/(\d+)/$', views.list, name='list'),
    # url(r'^detail/(\d+)/$', views.List.as_view(), name='detail'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^register/$', views.register, name='register'),
    url(r'^verfify/$', views.verfify, name='verfify'),
    url(r'^active/(.*?)/$', views.active, name='active'),


]
