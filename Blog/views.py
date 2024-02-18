from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog
# Create your views here.

class ListBlog(ListView):
    template_name = 'blog.html'
    model = Blog
    context_object_name = 'blog'
    
class DetailBlog(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'blog'
    
