from django.urls import path, re_path
from MyBlog.views import *

urlpatterns = [
    # path('base/', base),
    path('index/', index),
    path('about/', about),
    path('share/', share),
    path('list/', list),
    path('info/', info),
    path('gbook/', gbook),
    path('js/', js),
    path('article_api/', article_api),

    # path('add_art/', add_art),
]
