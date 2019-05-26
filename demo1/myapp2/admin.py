from django.contrib import admin
from .models import Poll,User
# Register your models here.

# 向admin注册myapp1的模型models
admin.site.register(Poll)
admin.site.register(User)
