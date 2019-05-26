from django.shortcuts import redirect,reverse

def checklogin(fun):
    def check(request, *args):
        # 在cookies中取用户
        # un = request.COOKIES.get("username")
        # 在session中取用户
        un = request.session.get("username")
        if un:
            return fun(request, *args)
        else:
            return redirect(reverse('roos: login'))

    return check