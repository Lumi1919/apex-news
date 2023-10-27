from django.shortcuts import render, HttpResponseRedirect, redirect
import requests
import http.client
from django.contrib.auth.models import User
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from .models import Post
from .models import Articles
from .models import A_voir
from .models import Album
from .models import Homme_de_la_semaine
from .models import Partenaires
from .models import Episode
from .models import Comment_Article
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
    articles = Articles.objects.all().order_by('-date')
    international_articles = Articles.objects.filter(article_categorie='international').order_by('-date')
    actu_articles = Articles.objects.filter(article_categorie='actualite').order_by('-date')
    societe_articles = Articles.objects.filter(article_categorie='societe').order_by('-date')
    politique_articles = Articles.objects.filter(article_categorie='politique').order_by('-date')
    sport_articles = Articles.objects.filter(article_categorie='sport').order_by('-date')
    culture_articles = Articles.objects.filter(article_categorie='culture').order_by('-date')
    cat_articles = Articles.objects.filter(article_categorie='activite').order_by('-date')
    spiritualite_articles = Articles.objects.filter(article_categorie='spiritualite').order_by('-date')
    partenaire = Partenaires.objects.all()
    videos = A_voir.objects.filter(categorie="activite").order_by('-date')
    
    context = {
        'videos': videos, 
        'partenaire': partenaire,
        'actu_articles': actu_articles,
        'societe_articles': societe_articles,
        'politique_articles': politique_articles,
        'sport_articles': sport_articles,
        'culture_articles': culture_articles,
        'spiritualite_articles': spiritualite_articles,
        'international_articles': international_articles,
        'cat_articles': cat_articles,
        'articles': articles,
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
    posts = Post.objects.all().order_by('-date')
    articles = Articles.objects.all().order_by('-date')
    cat_articles = Articles.objects.filter(article_categorie='sport').order_by('-date')
    

    if categorie is None:
        context = {
        'player_of_week': player_of_week, 
        'posts':posts, 
        'videos': videos,
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


def societe(request):
    user = request.user
    international_articles = Articles.objects.filter(article_categorie='international').order_by('-date')
    actu_articles = Articles.objects.filter(article_categorie='actualite').order_by('-date')
    societe_articles = Articles.objects.filter(article_categorie='societe').order_by('-date')
    politique_articles = Articles.objects.filter(article_categorie='politique').order_by('-date')
    sport_articles = Articles.objects.filter(article_categorie='sport').order_by('-date')
    culture_articles = Articles.objects.filter(article_categorie='culture').order_by('-date')
    spiritualite_articles = Articles.objects.filter(article_categorie='spiritualite').order_by('-date')
    partenaire = Partenaires.objects.all()
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
        'articles':articles, 
        'videos': videos, 
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
    activite_articles = Articles.objects.filter(article_categorie='activite').order_by('-date')
    partenaire = Partenaires.objects.all()
    articles = Articles.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="culture")
    cat_articles = Articles.objects.filter(article_categorie='culture').order_by('-date')
    
    context = {
        'videos': videos,
        'activites' : activites,
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
        'activite_articles': activite_articles,
        
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
    partenaire = Partenaires.objects.all()
    articles = Articles.objects.all().order_by('-date')
    videos = A_voir.objects.filter(categorie="societe").order_by('-date')
    cat_articles = Articles.objects.filter(article_categorie='politique').order_by('-date')
    
    context = {
        'videos': videos,
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
    return render(request, 'politique.html', context)


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

