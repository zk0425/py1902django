from django.conf.urls import url
from . import views
app_name = "root"
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^reg/$', views.reg, name='reg'),
    url(r'^list/$', views.list, name='list'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^deletebook/(\d+)/$', views.deletebook, name='deletebook'),
    url(r'^deletehero/(\d+)/$', views.deletehero, name='deletehero'),
    url(r'^addbook/(\d+)/$', views.addbook, name='addbook'),
    url(r'^addhero/(\d+)/$', views.addhero, name='addhero'),
    url(r'^updatehero/(\d+)/$', views.updatehero, name='updatehero'),

]
