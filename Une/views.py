from django.shortcuts import render
from home.models import Post
from home.models import Episode

def index(request):
    posts = Post.objects.all()
    episode = Episode.objects.all()
    return render(request, 'Une/index.html', {'posts': posts, 'episode': episode})
