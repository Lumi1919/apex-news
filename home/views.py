from django.shortcuts import render, HttpResponseRedirect, redirect
import requests
import http.client
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from .models import Post
from .models import Actu
from .models import Societe
from .models import Culture
from .models import People
from .models import Breaking
from .models import International
from .models import Articles
from .models import Activite
from .models import Event
from .models import Sport
from .models import A_voir
from .models import FootPlayerofWeek
from .models import FootPost
from .models import Album
from .models import Crew
from .models import FootPlayerofWeek
from .models import Gaming
from .models import Episode
from .models import Comment
from .models import Comment_Actu
from .models import Lamb
from .models import Lamb_combat
from .models import GameComment
from .forms import UserForm
from .forms import NewCommentForm
from datetime import datetime, timedelta, time


def index(request):
    user = request.user
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def articles(request, id):
    user = request.user
    articles = Articles.objects.all()
    article = Articles.objects.get(pk=id)
    return render(request, 'article.html', {'articles': articles, 'article': article})

def activites(request):
    user = request.user
    activites = Activite.objects.all().order_by('-date')
    coup_de_coeur = Activite.objects.all().order_by('-date')
    events = Event.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="activite").order_by('-date')
    return render(request, 'activites.html', {'activites': activites, 'videos': videos, 'events': events, 'coup_de_coeur': coup_de_coeur})

def sport(request, categorie=None):
    user = request.user
    player_of_week = FootPlayerofWeek.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="sport").order_by('-date')
    posts = Post.objects.all().order_by('-date')
    if categorie is None:
        sports = Sport.objects.all().order_by('-date')
        return render(request, 'sport.html', {'sports': sports, 'player_of_week': player_of_week, 'posts':posts, 'videos': videos})
    else:
        pass


def sport_show(request, id):
    user = request.user
    sport = Sport.objects.get(pk=id)
    sports = Sport.objects.all().order_by('-date')
    posts = Post.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="sport").order_by('-date')
    return render(request, 'sport_show.html', {'sport': sport, 'videos': videos, 'posts': posts, 'sports': sports})


def activite_show(request, id):
    user = request.user
    activite = Activite.objects.get(pk=id)
    coup_de_coeur = Activite.objects.all().order_by('-date')
    events = Event.objects.all()
    videos = A_voir.objects.filter(categorie="activite").order_by('-date')
    return render(request, 'activite_show.html', {'sport': sport, 'videos': videos, 'activite': activite, 'events': events, 'coup_de_coeur': coup_de_coeur})


def people_show(request, id):
    user = request.user
    people = People.objects.get(pk=id)
    peoples = People.objects.all().order_by('-date')
    societes = Societe.objects.all().order_by('-date')
    posts = Post.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="sport").order_by('-date')
    return render(request, 'people_show.html', {'people': people, 'peoples': peoples, 'videos': videos, 'posts': posts, 'societes': societes})


def societe(request):
    user = request.user
    societes = Societe.objects.all().order_by('-date')
    internationals = International.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="societe").order_by('-date')
    articles = Articles.objects.all().order_by('-date')
    return render(request, 'societe.html', {'societes': societes, 'articles':articles, 'videos': videos, 'internationals': internationals})


def international_show(request, id):
    user = request.user
    international = International.objects.get(pk=id)
    internationals = International.objects.all().order_by('-date')
    return render(request, 'international_show.html', {'international': international, 'internationals': internationals})

def societe_show(request, id):
    user = request.user
    societe = Societe.objects.get(pk=id)
    internationals = International.objects.all().order_by('-date')
    articles = Articles.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="societe").order_by('-date')
    return render(request, 'societe_show.html', {'societe': societe, 'videos': videos, 'articles':articles, 'internationals': internationals})


def culture(request):
    user = request.user
    cultures = Culture.objects.all().order_by('-date')
    peoples = People.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="culture")
    return render(request, 'culture.html', {'cultures': cultures, 'peoples': peoples, 'videos': videos})


def culture_show(request, id):
    user = request.user
    cultures = Culture.objects.all().order_by('-date')
    peoples = People.objects.all().order_by('-date')
    culture = Culture.objects.get(pk=id)
    videos = A_voir.objects.filter(categorie="culture").order_by('-date')
    return render(request, 'culture_show.html', {'culture': culture, 'videos': videos, 'peoples': peoples, 'cultures': cultures})


def emploi(request):
    user = request.user
    cultures = Culture.objects.all().order_by('-date')
    peoples = People.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="culture").order_by('-date')
    return render(request, 'emploi.html', {'culture': culture, 'videos': videos, 'peoples': peoples, 'cultures': cultures})



def breaking_show(request, id):
    user = request.user
    actus = Actu.objects.all().order_by('-date')
    breakings = Breaking.objects.all().order_by('-date')
    breaking = Breaking.objects.get(pk=id)
    videos = A_voir.objects.filter(categorie="culture").order_by('-date')
    return render(request, 'breaking_show.html', {'actus': actus, 'videos': videos, 'breaking': breaking, 'breakings': breakings})

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


def actu(request, id):
    user = request.user
    actu = get_object_or_404(Actu, pk=id)
    actus = Actu.objects.all().order_by('-date')
    actu_comments = Comment_Actu.objects.filter(actu=actu.id)
    new_comment = None
    if request.method == 'POST':
        comment_form = NewCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.actu = actu
            new_comment.save()
    else:
        comment_form = NewCommentForm()
    print()


    return render(request, 'actu.html', {'actu': actu, 'actus': actus, 'actu_comments': actu_comments, 'new_comment': new_comment, 'comment_form': comment_form})


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
    data = [{
        'HomeTeam': game["HomeTeam"],
        'AwayTeam': game["AwayTeam"],
        'GameId': game["GameID"],
        'Commentaire': (
                GameComment.objects.filter(game_id=game["GameID"]).first().pronostic if
                GameComment.objects.filter(game_id=game["GameID"]).first() else "Pas de pronostic Peundle pour l'instant..."
        )
    }
        for game in response
    ]

    return render(request, 'games.html', {'data' : data})


def lambPage(request):
    user = request.user
    combats = Lamb.objects.all()
    return render(request, 'lamb.html', {'combats': combats})

def showLamb(request, id):
    combat = Lamb.objects.get(pk=id)
    return render(request, 'combatshow.html', {'combat': combat})


def test_league_view(request):

    url = "https://v3.football.api-sports.io/leagues"
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    payload = {}
    headers = {
        'x-rapidapi-key': '5f08d06e4ae5171faea678b595f172b4',
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    conn.request("GET", "/leagues/seasons", headers=headers)
    res = conn.getresponse()

    # print(response.text)
    return render(request, 'test_league_view.html', {'data': response, 'res':res})
