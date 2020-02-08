from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from MyBlog.models import *
from django.core.paginator import Paginator
import time


# Create your views here.
# 父类视图测试
def base(request):
    course = Course.objects.first()
    id = course.id
    print(id)
    return render(request, 'myblog/base.html', locals())


# 首页
def index(request):
    tags = Course.objects.all()  # 标签云
    course = tags[:5]  # 大图
    recommend_art = Article.objects.filter(art_recommend=1)[0:6]  # 推荐的文章
    click_art = Article.objects.order_by('-art_click')[0:6]  # 点击率排行
    # article = Article.objects.order_by('-art_date').all()[:14]  # 所有文章

    return render(request, 'myblog/index.html', locals())


# 关于我
def about(request):
    return render(request, 'myblog/about.html')


# 我与她
def share(request):
    course = Course.objects.all()
    citys = City.objects.all()
    city_id = request.GET.get('id')
    if city_id:
        # print(city_id)
        images = Images.objects.filter(images_type=city_id).all()
    # print(city)
    return render(request, 'myblog/share.html', locals())


from django.db.models import Q


# 学无止境
def list(request):
    tags = Course.objects.all()
    course = Course.objects.all()
    req_id = request.GET.get('type_id')  # 获取请求的文章类型id
    type_art = Article.objects.filter(art_type=req_id).order_by('-art_date').all()  # 获取请求同类型文章的所有数据
    article = type_art.first()
    art_id = request.GET.get('art_id')  # 获取文章id
    page = request.GET.get('page')
    if not req_id and not page:
        type_art = Article.objects.filter(art_type=1).order_by('-art_date').all()
        click_art = Article.objects.filter(art_type=1).order_by('-art_click')[0:6]
        page = 1
    elif req_id and page:
        click_art = Article.objects.filter(art_type_id=req_id).order_by('-art_click')[0:6]
    elif art_id:  # 对请求是否有文章id进行判断
        # 如果有id，则对该文章处于该类型下文章的第几条进行统计，通过计数id<=art_id的个数，就是这篇文章处在第几条
        num = Article.objects.filter(Q(art_type=req_id) & Q(id__lte=art_id)).order_by('-art_date').count()
        click_art = Article.objects.filter(art_type_id=req_id).order_by('-art_click')[0:6]
        page = num // 5 + 1  # 用得到的在第几条进行计算，得到这篇文章处于第几页
    else:
        # 如果没有id，则用请求的page参数进行计算
        page = request.GET.get('page')
    paginator = Paginator(type_art, 7)  # 设置每页显示多少条数据，返回paginator对象
    page_obj = paginator.page(page)  # 指定页码的一个对象, <page 1 to 7>
    number = page_obj.number  # 控制可迭代的总页数，并且当前页显示在最中间
    start = number - 2
    end = number + 1
    if number <= 2:
        start = 0
        end = 3
    elif number >= paginator.num_pages - 2:
        end = paginator.num_pages
        start = end - 3
    page_range = paginator.page_range[start:end]

    return render(request, 'myblog/list.html', locals())


# 内容详情
def info(request):
    req_id = request.GET.get('id')
    art_list = []
    if req_id:
        art = Article.objects.filter(id=req_id).first()
        arts = Article.objects.filter(art_type=art.art_type)
    else:
        art = Article.objects.filter(id=1).first()
        arts = Article.objects.filter(art_type=art.art_type)
    for one in arts:
        art_list.append(one)
    a = art_list.index(art)  # 获取当前文章的索引
    if a == 0:
        shang_page = None
        xia_page = art_list[a + 1]
    else:
        shang_page = art_list[a - 1]
        print(shang_page, '---')
        b = a + 1
        if b < len(art_list):
            xia_page = art_list[b]
        else:
            xia_page = None
    art.art_click += 1
    art.save()

    return render(request, 'myblog/info.html', locals())


# 留言板
def gbook(request):
    comment = Comment.objects.order_by('-id').all()
    if request.method == 'POST':
        com = request.POST.get('com')
        # print(com)
        date = time.time()
        # print(date)
        comm = Comment()
        comm.comment = com
        comm.date = date
        comm.save()
    return render(request, 'myblog/gbook.html', locals())


def comment_api(request):
    com_obj_list = Comment.objects.order_by('-id').all()
    res = []
    for com_obj in com_obj_list:
        res.append({
            "comment": com_obj.comment,
            "date": com_obj.date
        })
    result = dict(res=res)
    return JsonResponse(result)


def article_api(request):
    page = int(request.GET.get('page'))
    start = (int(page) - 1) * 12
    end = start + 12
    article = Article.objects.order_by('-art_date').all()[start:end]
    res = []
    for article in article:
        img = str(article.art_img)
        date = str(article.art_date)
        # print(date)
        res.append({
            "id": article.id,
            "art_img": img,
            "art_title": article.art_title,
            "art_description": article.art_description,
            "art_type_id": article.art_type_id,
            "art_type": article.art_type.course_name,
            "art_date": date,
            "art_click": article.art_click,
        })
    result = dict(res=res)
    return JsonResponse(result)


# def js(request):
#     from django.core.serializers import serialize
#     # 获取页码
#     pn = request.GET.get('pn')
#     start = (int(pn) - 1) * 14
#     end = start + 14
#
#     article = Article.objects.order_by('-art_date').all()[start:end]
#     json_data = serialize('json', article)
#     # print(json_data)
#     return HttpResponse(json_data)


# 批量添加数据
import random

# def add_art(request):
#     for one in range(30):
#         article = Article()
#         article.art_title = '陌上花开，可缓缓归矣' + '%d' % one
#         article.art_description = '<p>用最简单的代码，实现瀑布流布局，没有繁琐的css，没有jq，看成是三列布局，分别用三个ul来调用。帝国cms列表模板，...</p>'
#         article.art_content = '<p>用最简单的代码，实现瀑布流布局，没有繁琐的css，没有jq，只需要做到以下就可以实现瀑布流的效果。思路很简单，看成是三列布局，分别用三个ul来调用。帝国cms列表模板。用最简单的代码，实现瀑布流布局，没有繁琐的css，没有jq，只需要做到以下就可以实现瀑布流的效果。思路很简单，看成是三列布局，分别用三个ul来调用。帝国cms列表模板，...用最简单的代码，实现瀑布流布局，没有繁琐的css，没有jq，只需要做到以下就可以实现瀑布流的效果。思路很简单，看成是三列布局，分别用三个ul来调用。帝国cms列表模板，...用最简单的代码，实现瀑布流布局，没有繁琐的css，没有jq，只需要做到以下就可以实现瀑布流的效果。思路很简单，看成是三列布局，分别用三个ul来调用。帝国cms列表模板，...用最简单的代码，实现瀑布流布局，没有繁琐的css，没有jq，只需要做到以下就可以实现瀑布流的效果。思路很简单，看成是三列布局，分别用三个ul来调用。帝国cms列表模板，...</p>'
#         article.art_img = 'images/text02.jpg'
#         article.art_type_id = random.choice([1, 2, 3, 4, 5, 6])
#         article.save()
#     return HttpResponse('增加数据成功')
