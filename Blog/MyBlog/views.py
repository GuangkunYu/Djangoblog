from django.shortcuts import render


# Create your views here.
# 父类视图测试
def base(request):
    return render(request, 'myblog/base.html')


# 首页
def index(request):
    return render(request, 'myblog/index.html')


# 关于我
def about(request):
    return render(request, 'myblog/about.html')


# 知识分享
def share(request):
    return render(request, 'myblog/share.html')


# 学无止境
def list(request):
    return render(request, 'myblog/list.html')


# 我与她
def info(request):
    return render(request, 'myblog/info.html')


# 留言板
def gbook(request):
    return render(request, 'myblog/gbook.html')
