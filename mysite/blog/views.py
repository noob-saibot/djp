from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Post, WikiInform, Charts
from django.views.generic import ListView, DetailView
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
import blog.wiki_parser as wiki

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PostsListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class Tree(TemplateView):
    template_name = "Tree.html"

class WikiPostDetail(ListView):
    model = WikiInform

class ChartsDetail(DetailView):
    model = Charts

class ChartsList(ListView):
    model = Charts

@never_cache
@csrf_exempt
def Notes(request):
    if request.method == "GET":
        id = request.GET.get('id')
        W = wiki.Inform(Post.objects.get(pk=id).content)
        try:
            return JsonResponse(W.links())
        except:
            pass
