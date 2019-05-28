from django.conf.urls import url
from . import views
app_name = "food"
urlpatterns = [

    url(r'^blog/$', views.blog, name="blog"),
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^gallery/$', views.gallery, name="gallery"),
    url(r'^login/$', views.login, name="login"),
    url(r'^register/$', views.register, name="register"),
    url(r'^single/$', views.single, name="single"),
    url(r'^index/$', views.index, name="index"),

]