from django.shortcuts import render, HttpResponseRedirect, redirect
import requests
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from .models import Post
from .models import Crew
from .models import Episode
from .models import Comment
from .models import Game_comment
from .forms import UserForm
from .forms import NewCommentForm
from datetime import datetime, timedelta, time




def index(request):
    user = request.user
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def showpost(request, id):
    user = request.user
    post = get_object_or_404(Post, pk=id)
    comments = Comment.objects.filter(post=post.id)
    new_comment = None
    if request.method == 'POST':
        comment_form = NewCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = NewCommentForm()
    print()

    return render(request, 'show.html', {'post': post, 'comments': comments,  'new_comment': new_comment, 'comment_form': comment_form})



def the_crew(request):
    user = request.user
    members = Crew.objects.all()
    return render(request, 'the_crew.html', {'members': members})


def crew_member(request, id):
    user = request.user
    member = Crew.objects.get(pk=id)
    return render(request, 'crew_member.html', {'member': member})


def explore(request):
    user = request.user
    posts = Post.objects.all()
    return render(request, 'explore.html', {'posts' : posts})


def podcast(request):
    user = request.user
    episodes = Episode.objects.all()
    return render(request, 'podcast.html', {'episodes' : episodes})

def podcastshow(request, id):
    user = request.user
    episode = Episode.objects.get(pk=id)
    return render(request, 'podcastshow.html', {'episode': episode})

def contact(request):
    return render(request, 'contact.html')

def register(request):
    user = request.user
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html')
    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        user = authenticate(request, username=username, email=email)
        if user is not None:
            login(request, user)
            return redirect('home:index')
    return render(request, 'login.html', context)


def logout(request):
    django_logout(request)
    return redirect('home:index')


def games(request):
    today = str(datetime.now().date())
    response = requests.get("https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/"+today+"?key=e308c3c08c5746af87dd48d80266337a").json()
    return render(request, 'games.html', {'response' : response})
