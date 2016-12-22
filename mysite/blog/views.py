from django.shortcuts import render
from django.views.generic import TemplateView
from blog.models import Post
from django.views.generic import ListView, DetailView

class PostsListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class Tree(TemplateView):
    template_name = "D3 Tree.html"
