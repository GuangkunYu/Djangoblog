from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# 测试demo
def demo(request):
    return HttpResponse('路由配置正确')


# 父页面
def base(request):
    return render(request, 'myblogapp/base.html')


# 主页
def index(request):
    return render(request, 'myblogapp/index.html')
