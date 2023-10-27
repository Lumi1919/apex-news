from django.shortcuts import render
from home.models import Post
from home.models import Articles
from home.models import A_voir
from home.models import Episode
from home.models import Album
from home.models import Partenaires
from home.models import Homme_de_la_semaine
from home.models import Comment_Article
from datetime import datetime
import requests

def mainpage(request):
    partenaire = Partenaires.objects.all()
    posts = Post.objects.all().order_by('-date')
    articles = Articles.objects.all().order_by('-date')
    videos = A_voir.objects.all().order_by('-date')
    episode = Episode.objects.all()
    album = Album.objects.all().order_by('-date')
    today = str(datetime.now().date())
    actu_articles = Articles.objects.filter(article_categorie='actualite').order_by('-date')
    societe_articles = Articles.objects.filter(article_categorie='societe').order_by('-date')
    politique_articles = Articles.objects.filter(article_categorie='politique').order_by('-date')
    sport_articles = Articles.objects.filter(article_categorie='sport').order_by('-date')
    culture_articles = Articles.objects.filter(article_categorie='culture').order_by('-date')
    spiritualite_articles = Articles.objects.filter(article_categorie='spiritualite').order_by('-date')
    international_articles = Articles.objects.filter(article_categorie='international').order_by('-date')
    homme_articles = Articles.objects.filter(article_categorie='homme_de_la_semaine').order_by('-date')
    breaking_articles = Articles.objects.filter(article_categorie='breaking').order_by('-date')

    context = {
        'posts': posts,
        'partenaire': partenaire,
        'articles': articles,
        'album': album,
        'videos': videos,
        'actu_articles': actu_articles,
        'societe_articles': societe_articles,
        'politique_articles': politique_articles,
        'sport_articles': sport_articles,
        'culture_articles': culture_articles,
        'spiritualite_articles': spiritualite_articles,
        'international_articles': international_articles,
        'homme_articles': homme_articles,
        'breaking_articles': breaking_articles,
    }
    return render(request, 'main/index.html', context)

