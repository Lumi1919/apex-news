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
    international_articles = Articles.objects.filter(article_categorie='international').order_by('-date')
    actu_articles = Articles.objects.filter(article_categorie='actualite').order_by('-date')
    societe_articles = Articles.objects.filter(article_categorie='societe').order_by('-date')
    politique_articles = Articles.objects.filter(article_categorie='politique').order_by('-date')
    sport_articles = Articles.objects.filter(article_categorie='sport').order_by('-date')
    culture_articles = Articles.objects.filter(article_categorie='culture').order_by('-date')
    spiritualite_articles = Articles.objects.filter(article_categorie='spiritualite').order_by('-date')
    article = Articles.objects.get(pk=id)
    post_views = None
    comments_num = None
    if article:
        article.post_views = article.post_views + 1
        article.save()
    comments = Comment_Article.objects.filter(article=article.id).order_by('-date')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        new_comment = Comment_Article(name=name, email=email, content=content)
        new_comment.article = article
        new_comment.save()

        if new_comment: 
            article.comments_num = article.comments_num + 1
            article.save()
            
        return redirect(request.path)
    comments_count = Comment_Article.objects.filter(article=article.id).count()
    context = {
        'articles': articles,
        'article': article, 
        'videos': videos, 
        'cultures': cultures, 
        'partenaire' : partenaire, 
        'comments' : comments,
        'comments_count' : comments_count,
        'actu_articles': actu_articles,
        'societe_articles': societe_articles,
        'politique_articles': politique_articles,
        'sport_articles': sport_articles,
        'culture_articles': culture_articles,
        'spiritualite_articles': spiritualite_articles,
        'international_articles': international_articles,
        'post_views': post_views,
    }
    
    return render(request, 'article.html', context)

def activites(request):
    user = request.user
    international_articles = Articles.objects.filter(article_categorie='international').order_by('-date')
    actu_articles = Articles.objects.filter(article_categorie='actualite').order_by('-date')
    societe_articles = Articles.objects.filter(article_categorie='societe').order_by('-date')
    politique_articles = Articles.objects.filter(article_categorie='politique').order_by('-date')
    sport_articles = Articles.objects.filter(article_categorie='sport').order_by('-date')
    culture_articles = Articles.objects.filter(article_categorie='culture').order_by('-date')
    cat_articles = Articles.objects.filter(article_categorie='activite').order_by('-date')
    spiritualite_articles = Articles.objects.filter(article_categorie='spiritualite').order_by('-date')
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
        'partenaire': partenaire,
        'actu_articles': actu_articles,
        'societe_articles': societe_articles,
        'politique_articles': politique_articles,
        'sport_articles': sport_articles,
        'culture_articles': culture_articles,
        'spiritualite_articles': spiritualite_articles,
        'international_articles': international_articles,
        'cat_articles': cat_articles,
    }
    return render(request, 'activites.html', context)

def sport(request, categorie=None):
    user = request.user
    international_articles = Articles.objects.filter(article_categorie='international').order_by('-date')
    actu_articles = Articles.objects.filter(article_categorie='actualite').order_by('-date')
    societe_articles = Articles.objects.filter(article_categorie='societe').order_by('-date')
    politique_articles = Articles.objects.filter(article_categorie='politique').order_by('-date')
    sport_articles = Articles.objects.filter(article_categorie='sport').order_by('-date')
    culture_articles = Articles.objects.filter(article_categorie='culture').order_by('-date')
    spiritualite_articles = Articles.objects.filter(article_categorie='spiritualite').order_by('-date')
    activite_articles = Articles.objects.filter(article_categorie='activite').order_by('-date')
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
        'actu_articles': actu_articles,
        'societe_articles': societe_articles,
        'politique_articles': politique_articles,
        'sport_articles': sport_articles,
        'culture_articles': culture_articles,
        'spiritualite_articles': spiritualite_articles,
        'international_articles': international_articles,
        'activite_articles': activite_articles,
    }
        
        return render(request, 'sport.html', context)
    else:
        pass



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
    international_articles = Articles.objects.filter(article_categorie='international').order_by('-date')
    actu_articles = Articles.objects.filter(article_categorie='actualite').order_by('-date')
    societe_articles = Articles.objects.filter(article_categorie='societe').order_by('-date')
    politique_articles = Articles.objects.filter(article_categorie='politique').order_by('-date')
    sport_articles = Articles.objects.filter(article_categorie='sport').order_by('-date')
    culture_articles = Articles.objects.filter(article_categorie='culture').order_by('-date')
    spiritualite_articles = Articles.objects.filter(article_categorie='spiritualite').order_by('-date')
    societes = Societe.objects.all().order_by('-date')
    partenaire = Partenaires.objects.all()
    internationals = International.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="societe").order_by('-date')
    articles = Articles.objects.all().order_by('-date')
    cat_articles = Articles.objects.filter(article_categorie='societe').order_by('-date')
    
    context = {
        'actu_articles': actu_articles,
        'societe_articles': societe_articles,
        'politique_articles': politique_articles,
        'sport_articles': sport_articles,
        'culture_articles': culture_articles,
        'spiritualite_articles': spiritualite_articles,
        'international_articles': international_articles,
        'societes': societes, 
        'articles':articles, 
        'videos': videos, 
        'internationals': internationals, 
        'partenaire' : partenaire, 
        'cat_articles': cat_articles
    }
    return render(request, 'societe.html', context)


def culture(request):
    user = request.user
    international_articles = Articles.objects.filter(article_categorie='international').order_by('-date')
    actu_articles = Articles.objects.filter(article_categorie='actualite').order_by('-date')
    societe_articles = Articles.objects.filter(article_categorie='societe').order_by('-date')
    politique_articles = Articles.objects.filter(article_categorie='politique').order_by('-date')
    sport_articles = Articles.objects.filter(article_categorie='sport').order_by('-date')
    culture_articles = Articles.objects.filter(article_categorie='culture').order_by('-date')
    spiritualite_articles = Articles.objects.filter(article_categorie='spiritualite').order_by('-date')
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
        'actu_articles': actu_articles,
        'societe_articles': societe_articles,
        'politique_articles': politique_articles,
        'sport_articles': sport_articles,
        'culture_articles': culture_articles,
        'spiritualite_articles': spiritualite_articles,
        'international_articles': international_articles,
        
    }
    return render(request, 'culture.html', context)



def politique(request):
    international_articles = Articles.objects.filter(article_categorie='international').order_by('-date')
    actu_articles = Articles.objects.filter(article_categorie='actualite').order_by('-date')
    societe_articles = Articles.objects.filter(article_categorie='societe').order_by('-date')
    politique_articles = Articles.objects.filter(article_categorie='politique').order_by('-date')
    sport_articles = Articles.objects.filter(article_categorie='sport').order_by('-date')
    culture_articles = Articles.objects.filter(article_categorie='culture').order_by('-date')
    spiritualite_articles = Articles.objects.filter(article_categorie='spiritualite').order_by('-date')
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
        'actu_articles': actu_articles,
        'societe_articles': societe_articles,
        'politique_articles': politique_articles,
        'sport_articles': sport_articles,
        'culture_articles': culture_articles,
        'spiritualite_articles': spiritualite_articles,
        'international_articles': international_articles,
    }
    return render(request, 'politique.html', context)



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
    international_articles = Articles.objects.filter(article_categorie='international').order_by('-date')
    actu_articles = Articles.objects.filter(article_categorie='actualite').order_by('-date')
    societe_articles = Articles.objects.filter(article_categorie='societe').order_by('-date')
    politique_articles = Articles.objects.filter(article_categorie='politique').order_by('-date')
    sport_articles = Articles.objects.filter(article_categorie='sport').order_by('-date')
    culture_articles = Articles.objects.filter(article_categorie='culture').order_by('-date')
    cat_articles = Articles.objects.filter(article_categorie='homme_de_la_semaine').order_by('-date')
    spiritualite_articles = Articles.objects.filter(article_categorie='spiritualite').order_by('-date')
    videos = A_voir.objects.filter(categorie="culture").order_by('-date')
    
    context = {
        'actu_articles': actu_articles,
        'societe_articles': societe_articles,
        'politique_articles': politique_articles,
        'sport_articles': sport_articles,
        'culture_articles': culture_articles,
        'spiritualite_articles': spiritualite_articles,
        'international_articles': international_articles,
        'homme': homme, 
        'videos': videos,
        'cat_articles': cat_articles,
    }
    
    
    return render(request, 'homme_show.html', context)


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

