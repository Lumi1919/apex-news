from django.shortcuts import render
from home.models import Post
from home.models import Articles
from home.models import Evenements_Jour
from home.models import Activite
from home.models import People
from home.models import A_voir
from home.models import Breaking
from home.models import Episode
from home.models import Album
from home.models import Actu
from home.models import Sport
from home.models import Societe
from home.models import Culture, Partenaires
from home.models import International
from home.models import Homme_de_la_semaine
from home.models import Comment_Article
from datetime import datetime
import requests

def mainpage(request):
    partenaire = Partenaires.objects.all()
    posts = Post.objects.all().order_by('-date')
    societes = Societe.objects.all().order_by('-date')
    cultures = Culture.objects.all().order_by('-date')
    internationals = International.objects.all().order_by('-date')
    articles = Articles.objects.all().order_by('-date')
    evenements = Evenements_Jour.objects.all().order_by('-date')
    videos = A_voir.objects.all().order_by('-date')
    sports = Sport.objects.all().order_by('-date')
    episode = Episode.objects.all()
    album = Album.objects.all().order_by('-date')
    activites = Activite.objects.all().order_by('-date')
    breakings = Breaking.objects.all().order_by('-date')
    peoples = People.objects.all().order_by('-date')
    actus = Actu.objects.all().order_by('-date')
    today = str(datetime.now().date())
    actu_articles = Articles.objects.filter(article_categorie='actualite').order_by('-date')
    societe_articles = Articles.objects.filter(article_categorie='societe').order_by('-date')
    politique_articles = Articles.objects.filter(article_categorie='politique').order_by('-date')
    sport_articles = Articles.objects.filter(article_categorie='sport').order_by('-date')
    culture_articles = Articles.objects.filter(article_categorie='culture').order_by('-date')
    spiritualite_articles = Articles.objects.filter(article_categorie='spiritualite').order_by('-date')
    international_articles = Articles.objects.filter(article_categorie='international').order_by('-date')
    homme_articles = Articles.objects.filter(article_categorie='homme_de_la_semaine').order_by('-date')

    # response = requests.get("https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/"+today+"?key=e308c3c08c5746af87dd48d80266337a").json()
    #data = [{
    #    'HomeTeam': game["HomeTeam"],
    #    'AwayTeam': game["AwayTeam"],
    #   'GameId': game["GameID"],
    #    'DateTime': game["DateTime"],
    #   'Commentaire': (
    #            GameComment.objects.filter(game_id=game["GameID"]).first().pronostic if
    #           GameComment.objects.filter(game_id=game["GameID"]).first() else "Pas de pronostic Peundle pour l'instant..."
    #   )
    #}
    #    for game in response
    #]
    context = {
        'posts': posts,
                   'partenaire': partenaire,
                   'articles': articles,
                   'evenements': evenements,
                   'album': album,
                   'activites': activites,
                   'peoples': peoples,
                   'actus': actus,
                   'sports': sports,
                   'societes': societes,
                   'cultures' : cultures,
                   'internationals': internationals,
                   'videos': videos,
                   'breakings': breakings,
                   'actu_articles': actu_articles,
                   'societe_articles': societe_articles,
                   'politique_articles': politique_articles,
                   'sport_articles': sport_articles,
                   'culture_articles': culture_articles,
                   'spiritualite_articles': spiritualite_articles,
                   'international_articles': international_articles,
                    'homme_articles': homme_articles,
    }
    return render(request, 'main/index.html', context)

