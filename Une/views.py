from django.shortcuts import render
from home.models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'Une/index.html', {'posts': posts})
