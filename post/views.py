from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Post

# Create your views here.

class BlogListView(ListView):
    model=Post
    template_name='index.html'
    ordering=['-count']
    
def Counter(request, pk):
    item = Post.objects.get(id=pk)
    item.count += 1
    item.save()
    return redirect(item.link)


