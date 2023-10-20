from django.shortcuts import render, HttpResponseRedirect, redirect
import requests
import http.client
from django.contrib.auth.models import User
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from .models import Post
from .models import Actu
from .models import Societe
from .models import Culture
from .models import Politique
from .models import People
from .models import Breaking
from .models import International
from .models import Articles
from .models import Activite
from .models import Event
from .models import Sport
from .models import A_voir
from .models import Album
from .models import Homme_de_la_semaine
from .models import Partenaires
from .models import Episode
from .models import Comment
from .models import Comment_Article
from .forms import UserForm
from .forms import NewCommentForm
from datetime import datetime, timedelta, time


def index(request):
    user = request.user
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def articles(request, id):
    user = request.user
    articles = Articles.objects.all().order_by('-date')
    partenaire = Partenaires.objects.all()
    videos = A_voir.objects.filter(categorie="societe").order_by('-date')
    cultures = Culture.objects.all().order_by('-date')
    article = Articles.objects.get(pk=id)
    article_view = article.post_views + 1
    article.save()
    comments = Comment_Article.objects.filter(article=article.id).order_by('-date')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
  
        new_comment = Comment_Article(name=name, email=email, content=content)
        new_comment.article = article
        new_comment.save()
        return redirect(request.path)
    comments_count = Comment_Article.objects.filter(article=article.id).count()
    context = {
        'articles': articles,
        'article': article, 
        'videos': videos, 
        'cultures': cultures, 
        'partenaire' : partenaire, 
        'article_view': article_view,
        'comments' : comments,
        'comments_count' : comments_count,
    }
    
    return render(request, 'article.html', context)

def activites(request):
    user = request.user
    activites = Activite.objects.all().order_by('-date')
    partenaire = Partenaires.objects.all()
    coup_de_coeur = Activite.objects.all().order_by('-date')
    events = Event.objects.all().order_by('-date')
    peoples = People.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="activite").order_by('-date')
    
    context = {
        'activites': activites, 
        'videos': videos, 
        'events': events, 
        'peoples': peoples,
        'partenaire': partenaire
    }
    return render(request, 'activites.html', context)

def sport(request, categorie=None):
    user = request.user
    partenaire = Partenaires.objects.all()
    player_of_week = Homme_de_la_semaine.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="sport").order_by('-date')
    events = Event.objects.all().order_by('-date')
    cultures = Culture.objects.all().order_by('-date')
    posts = Post.objects.all().order_by('-date')
    articles = Articles.objects.all().order_by('-date')
    cat_articles = Articles.objects.filter(article_categorie='sport').order_by('-date')
    

    if categorie is None:
        sports = Sport.objects.all().order_by('-date')
        context = {
        'sports':sports,
        'player_of_week': player_of_week, 
        'posts':posts, 
        'videos': videos,
        'cultures':cultures,
        'events': events,
        'partenaire' : partenaire,
        'articles': articles,
        'cat_articles': cat_articles,
    }
        
        return render(request, 'sport.html', context)
    else:
        pass


def sport_show(request, id):
    user = request.user
    sport = Sport.objects.get(pk=id)
    partenaire = Partenaires.objects.all()
    events = Event.objects.all().order_by('-date')
    cultures = Culture.objects.all().order_by('-date')
    sports = Sport.objects.all().order_by('-date')
    posts = Post.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="sport").order_by('-date')
    
    context = {
        'sport': sport, 
        'videos': videos, 
        'posts': posts, 
        'sports': sports,
        'cultures': cultures,
        'events': events,
        'partenaire' : partenaire,
    }
    return render(request, 'sport_show.html', context)


def activite_show(request, id):
    user = request.user
    partenaire = Partenaires.objects.all()
    activite = Activite.objects.get(pk=id)
    activites = Activite.objects.all().order_by('-date')
    peoples = People.objects.all().order_by('-date')
    events = Event.objects.all()
    videos = A_voir.objects.filter(categorie="activite").order_by('-date')
    
    context = {
        'sport': sport, 
        'partenaire': partenaire,
        'videos': videos, 
        'activite': activite, 
        'events': events, 
        'activites': activites, 
        'peoples' : peoples,
        'events' : events, 
    }
    return render(request, 'activite_show.html', context)


def people_show(request, id):
    user = request.user
    people = People.objects.get(pk=id)
    peoples = People.objects.all().order_by('-date')
    activites = Activite.objects.all().order_by('-date')
    articles = Articles.objects.all().order_by('-date')
    events = Event.objects.all().order_by('-date')
    societes = Societe.objects.all().order_by('-date')
    partenaire = Partenaires.objects.all()
    posts = Post.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="sport").order_by('-date')
    
    context = {
        'people': people, 
        'peoples': peoples, 
        'videos': videos, 
        'posts': posts, 
        'societes': societes,
        'events': events,
        'activites': activites,
        'articles': articles,
        'partenaire' : partenaire,
    }
    return render(request, 'people_show.html', context)


def societe(request):
    user = request.user
    societes = Societe.objects.all().order_by('-date')
    partenaire = Partenaires.objects.all()
    internationals = International.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="societe").order_by('-date')
    articles = Articles.objects.all().order_by('-date')
    cat_articles = Articles.objects.filter(article_categorie='societe').order_by('-date')
    return render(request, 'societe.html', {'societes': societes, 'articles':articles, 'videos': videos, 'internationals': internationals, 'partenaire' : partenaire, 'cat_articles': cat_articles})


def international_show(request, id):
    user = request.user
    international = International.objects.get(pk=id)
    internationals = International.objects.all().order_by('-date')
    societe = Societe.objects.get(pk=id)
    partenaire = Partenaires.objects.all()
    internationals = International.objects.all().order_by('-date')
    cultures = Culture.objects.all().order_by('-date')
    articles = Articles.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="societe").order_by('-date')
    
    
    context = {
        'international': international, 
        'internationals': internationals,
        'partenaire' : partenaire,
        'cultures' :cultures,
        'articles' : articles,
        'videos' : videos,
        'cultures' :cultures,
        'articles' : articles,
        
    }
        
    return render(request, 'international_show.html', context)

def societe_show(request, id):
    user = request.user
    societe = Societe.objects.get(pk=id)
    partenaire = Partenaires.objects.all()
    internationals = International.objects.all().order_by('-date')
    cultures = Culture.objects.all().order_by('-date')
    articles = Articles.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="societe").order_by('-date')
    
    context = {
        'societe': societe, 
        'videos': videos, 
        'articles':articles, 
        'internationals': internationals,
        'cultures' : cultures,
        'videos' : videos,
        'partenaire' : partenaire, 
    }
    return render(request, 'societe_show.html', context)


def culture(request):
    user = request.user
    cultures = Culture.objects.all().order_by('-date')
    partenaire = Partenaires.objects.all()
    peoples = People.objects.all().order_by('-date')
    activites = Activite.objects.all().order_by('-date')
    articles = Articles.objects.all().order_by('-date')
    events = Event.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="culture")
    cat_articles = Articles.objects.filter(article_categorie='culture').order_by('-date')
    
    context = {
        'cultures': cultures, 
        'peoples': peoples, 
        'videos': videos,
        'activites' : activites,
        'events': events,
        'articles': articles,
        'partenaire' : partenaire,
        'cat_articles' : cat_articles,
        
    }
    return render(request, 'culture.html', context)


def culture_show(request, id):
    cultures = Culture.objects.all().order_by('-date')
    events = Event.objects.all().order_by('-date')
    articles = Articles.objects.all().order_by('-date')
    peoples = People.objects.all().order_by('-date')
    activites = Activite.objects.all().order_by('-date')
    culture = Culture.objects.get(pk=id)
    partenaire = Partenaires.objects.all()
    videos = A_voir.objects.filter(categorie="societe").order_by('-date')
    
    context = {
        'videos': videos, 
        'cultures': cultures,
        'articles': articles,
        'culture' : culture,
        'events' : events,
        'activites' : activites,
        'partenaire' : partenaire,
    }
    return render(request, 'culture_show.html', context)



def politique(request):
    politiques = Politique.objects.all().order_by('-date')
    partenaire = Partenaires.objects.all()
    cultures = Culture.objects.all().order_by('-date')
    articles = Articles.objects.all().order_by('-date')
    internationals = International.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="societe").order_by('-date')
    cat_articles = Articles.objects.filter(article_categorie='politique').order_by('-date')
    
    context = {
        'cultures': cultures, 
        'videos': videos,
        'articles': articles,
        'politiques':politiques,
        'internationals' : internationals,
        'partenaire' : partenaire,
        'cat_articles' : cat_articles,
    }
    return render(request, 'politique.html', context)


def politique_show(request, id):
    cultures = Culture.objects.all().order_by('-date')
    internationals = International.objects.all().order_by('-date')
    articles = Articles.objects.all().order_by('-date')
    politiques = Politique.objects.all().order_by('-date')
    politique = Politique.objects.get(pk=id)
    partenaire = Partenaires.objects.all()
    comments = Comment.objects.filter(politique=politique.id)
    videos = A_voir.objects.filter(categorie="societe").order_by('-date')
    new_comment = None
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        comment = request.POST['comment']
  
        new_comment = Comment(name=name, email=mail, content=comment)
        new_comment.politique = politique
        new_comment.save()
        return redirect(request.path)
    else:
        comment_form = NewCommentForm()
    print()


    context = {
        'videos': videos, 
        'cultures': cultures,
        'articles': articles,
        'politique' : politique,
        'politiques' : politiques,
        'internationals' : internationals,
        'partenaire' : partenaire,
        'new_comment' : new_comment,
        'comments' : comments,
    }
    return render(request, 'politique_show.html', context)


def event_show(request, id):
    event = Event.objects.get(pk=id)
    partenaire = Partenaires.objects.all()
    events = Event.objects.all().order_by('-date')
    cultures = Culture.objects.all().order_by('-date')
    activites = Activite.objects.all().order_by('-date')
    articles = Articles.objects.all().order_by('-date')
    peoples = People.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="culture").order_by('-date')
    
    context = {
        'culture': culture, 
        'videos': videos, 'peoples': peoples, 
        'cultures': cultures,
        'peoples' : peoples,
        'events': events,
        'activites': activites,
        'articles': articles,
        'partenaire' : partenaire, 
        'event' : event,
        }
    return render(request, 'event_show.html', context)




def breaking_show(request, id):
    user = request.user
    actus = Actu.objects.all().order_by('-date')
    partenaire = Partenaires.objects.all()
    breakings = Breaking.objects.all().order_by('-date')
    breaking = Breaking.objects.get(pk=id)
    videos = A_voir.objects.filter(categorie="culture").order_by('-date')
    
    context = {
        'actus': actus, 
        'videos': videos, 
        'breaking': breaking, 
        'breakings': breakings, 
        'partenaire' : partenaire,
    }
    return render(request, 'breaking_show.html', context)


def homme_de_la_semaine_show(request, id):
    homme = Homme_de_la_semaine.objects.get(pk=id)
    videos = A_voir.objects.filter(categorie="culture").order_by('-date')
    return render(request, 'homme_show.html', {'homme': homme, 'videos': videos})



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
    actu = get_object_or_404(Actu, pk=id)
    actus = Actu.objects.all().order_by('-date')
    cultures = Culture.objects.all().order_by('-date')
    internationals = International.objects.all().order_by('-date')
    articles = Articles.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="societe").order_by('-date')
 

    context = {
        'actu': actu, 
        'actus': actus, 
        'videos': videos, 
        'articles': articles,
        'cultures': cultures, 
        'internationals': internationals,
    }


    return render(request, 'actu.html', context)



def podcast(request):
    user = request.user
    episodes = Episode.objects.all()
    return render(request, 'podcast.html', {'episodes' : episodes})

def podcastshow(request, id):
    user = request.user
    episode = Episode.objects.get(pk=id)
    return render(request, 'podcastshow.html', {'episode': episode})


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


def login(request):
    context = {}
    if request.method == 'POST':
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = authenticate(request, username=username, email=email)
        if user is not None:
            login(request, user)
            return redirect('home:index')
    return render(request, 'login.html', context)


def logout(request):
    django_logout(request)
    return redirect('home:index')







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
