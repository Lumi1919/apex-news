from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    url('the_crew/member/(?P<id>[0-9]+)$', views.crew_member, name='member'),
    url('podcast/(?P<id>[0-9]+)$', views.podcastshow, name='podcastshow'),
    url('article/(?P<id>[0-9]+)$', views.articles, name='article'),
    path('emploi/', views.emploi, name='emploi'),
    url('actu/(?P<id>[0-9]+)$', views.actu, name='actu'),
    path('podcast/', views.podcast, name='podcast'),
    url('combat/(?P<id>[0-9]+)$', views.showLamb, name='showLamb'),
    path('lamb', views.lambPage, name='lamb'),
    path('sport/', views.sport, name='sport'),
    path('societe/', views.societe, name='societe'),
    path('culture/', views.culture, name='culture'),
    url('sport/(?P<id>[0-9]+)$', views.sport_show, name='sport_show'),
    url('people/(?P<id>[0-9]+)$', views.people_show, name='people_show'),
    url('culture/(?P<id>[0-9]+)$', views.culture_show, name='culture_show'),
    url('societe/(?P<id>[0-9]+)$', views.societe_show, name='societe_show'),
    url('international/(?P<id>[0-9]+)$', views.international_show, name='international_show'),
    url('activite/(?P<id>[0-9]+)$', views.activite_show, name='activite_show'),
    url('breaking/(?P<id>[0-9]+)$', views.breaking_show, name='breaking_show'),
    path('the_crew/', views.the_crew, name='crew'),
    path('games/', views.games, name='games'),
    path('activites/', views.activites, name='activites'),
    path('explore/', views.explore, name='explore'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('test/', views.test_league_view, name='test_league_view'),
    url('post/(?P<id>[0-9]+)$', views.showpost, name='showpost'),
    path('', views.index, name='index'),
]

