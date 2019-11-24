from django.urls import path,re_path
from MyBlogApp.views import *

urlpatterns = [
    # path('demo/', demo),
    # re_path('^$', demo),
    # path('base/', base),
    path('index/', index),
]
