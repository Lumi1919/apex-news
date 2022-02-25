from django.shortcuts import render
from home.models import Post
from home.models import Articles
from home.models import Evenements_Jour
from home.models import FootPost
from home.models import Gaming
from home.models import Activite
from home.models import People
from home.models import A_voir
from home.models import Breaking
from home.models import Episode
from home.models import GameComment
from home.models import Lamb
from home.models import Lamb_combat
from home.models import Album
from home.models import Actu
from home.models import Sport
from home.models import Societe
from home.models import Culture
from home.models import International
from home.models import FootPlayerofWeek
from datetime import datetime
import requests

def mainpage(request):
    posts = Post.objects.all().order_by('-date')
    societes = Societe.objects.all().order_by('-date')
    cultures = Culture.objects.all().order_by('-date')
    internationals = International.objects.all().order_by('-date')
    articles = Articles.objects.all().order_by('-date')
    evenements = Evenements_Jour.objects.all().order_by('-date')
    foot_posts = FootPost.objects.all().order_by('-date')
    videos = A_voir.objects.all().order_by('-date')
    sports = Sport.objects.all().order_by('-date')
    episode = Episode.objects.all()
    player_of_week = FootPlayerofWeek.objects.all().order_by('-date')
    album = Album.objects.all().order_by('-date')
    activites = Activite.objects.all().order_by('-date')
    breakings = Breaking.objects.all().order_by('-date')
    peoples = People.objects.all().order_by('-date')
    actus = Actu.objects.all().order_by('-date')
    gaming_data = Gaming.objects.all().order_by('-date')
    lamb_posts = Lamb.objects.all().order_by('-date')
    combats = Lamb_combat.objects.all().order_by('-date')
    today = str(datetime.now().date())

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
    return render(request, 'main/index.html',
                  {'posts': posts,
                   'articles': articles,
                   'evenements': evenements,
                   'episode': episode,
                   'lamb_posts': lamb_posts,
                   'combats': combats,
                   'album': album,
                   'player_of_week': player_of_week,
                   'gaming_data': gaming_data,
                   'foot_posts': foot_posts,
                   'activites': activites,
                   'peoples': peoples,
                   'actus': actus,
                   'sports': sports,
                   'societes': societes,
                   'cultures' : cultures,
                   'internationals': internationals,
                   'videos': videos,
                   'breakings': breakings
                   }
                  )
