#coding: utf-8
from django.conf.urls import *
from django.views.generic import TemplateView
from blog.views import PostsListView, PostDetailView, Tree, Notes, WikiPostDetail

urlpatterns = [
url(r'^$', Tree.as_view(), name='tree'),
url(r'^main/$', PostsListView.as_view(), name='list'),
url(r'^main/(?P<pk>\d+)/$', PostDetailView.as_view()),
url(r'^api/$', Notes),
]
