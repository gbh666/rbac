from django.shortcuts import render,HttpResponse,redirect
from rbac import models as rbac_models
from rbac.service.init_permission import init_permission
from django.conf import settings

def log_in(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        user = request.POST.get("username")
        pwd = request.POST.get("password")

        user_obj = rbac_models.UserInfo.objects.filter(username=user,password=pwd).first()

        if not user_obj:
            return render(request,'login.html',{'msg':"用户名密码错误"})
        else:
            # 获取当前用户所有权限
            # 获取菜单
            # 写入session
            init_permission(request,user_obj)
            return redirect('/index.html')

def index(request):

    return HttpResponse("Index")

def menu(request):

    return render(request,'menu.html')