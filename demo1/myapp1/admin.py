from django.contrib import admin
from .models import Heroinfo, Bookinfo
# Register your models here.

# 向admin注册myapp1的模型models
admin.site.register(Heroinfo)
admin.site.register(Bookinfo)
