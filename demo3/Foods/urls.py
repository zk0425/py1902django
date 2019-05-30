from django.conf.urls import url
from . import views
app_name = "food"
urlpatterns = [

    url(r'^blog/$', views.blog, name="blog"),
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^gallery/$', views.gallery, name="gallery"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name="register"),
    url(r'^single/$', views.single, name="single"),
    url(r'^menu/$', views.menu, name="menu"),
    url(r'^index/$', views.index, name="index"),
    url(r'^text/$', views.text, name="text"),
    url(r'^error/$', views.error, name="error"),


]