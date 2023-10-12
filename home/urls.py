from django.conf.urls import url,re_path
from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    url('podcast/(?P<id>[0-9]+)$', views.podcastshow, name='podcastshow'),
    url('article/(?P<id>[0-9]+)$', views.articles, name='article'),
    url('actu/(?P<id>[0-9]+)$', views.actu, name='actu'),
    url('event/(?P<id>[0-9]+)$', views.event_show, name='event_show'),
    path('podcast/', views.podcast, name='podcast'),
    path('sport/', views.sport, name='sport'),
    path('societe/', views.societe, name='societe'),
    path('culture/', views.culture, name='culture'),
    path('politique/', views.politique, name='politique'),
    url('sport/(?P<id>[0-9]+)$', views.sport_show, name='sport_show'),
    url('homme_de_la_semaine/(?P<id>[0-9]+)$', views.homme_de_la_semaine_show, name='homme_de_la_semaine_show'),
    url('people/(?P<id>[0-9]+)$', views.people_show, name='people_show'),
    url('culture/(?P<id>[0-9]+)$', views.culture_show, name='culture_show'),
    url('societe/(?P<id>[0-9]+)$', views.societe_show, name='societe_show'),
    url('international/(?P<id>[0-9]+)$', views.international_show, name='international_show'),
    url('activite/(?P<id>[0-9]+)$', views.activite_show, name='activite_show'),
    url('politique/(?P<id>[0-9]+)$', views.politique_show, name='politique_show'),
    url('breaking/(?P<id>[0-9]+)$', views.breaking_show, name='breaking_show'),
    path('activites/', views.activites, name='activites'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('test/', views.test_league_view, name='test_league_view'),
    url('post/(?P<id>[0-9]+)$', views.showpost, name='showpost'),
    path('', views.index, name='index'),
]

