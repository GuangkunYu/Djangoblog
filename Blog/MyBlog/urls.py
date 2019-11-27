from django.urls import path
from MyBlog.views import *

urlpatterns = [
    # path('base/', base),
    path('index/', index),
    path('about/', about),
    path('share/', share),
    path('list/', list),
    path('info/', info),
    path('gbook/', gbook),
]
