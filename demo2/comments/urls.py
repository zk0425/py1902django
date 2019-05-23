from django.conf.urls import url
from . import views
app_name = "comments"
urlpatterns = [
    url(r'^adddiscuss/(\d+)/$', views.AddDiscuss.as_view(), name='adddiscuss')
]
