from django.conf.urls import url,re_path
from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    url('podcast/(?P<id>[0-9]+)$', views.podcastshow, name='podcastshow'),
    url('article/(?P<id>[0-9]+)$', views.articles, name='article'),
    path('podcast/', views.podcast, name='podcast'),
    path('sport/', views.sport, name='sport'),
    path('societe/', views.societe, name='societe'),
    path('culture/', views.culture, name='culture'),
    path('politique/', views.politique, name='politique'),
    url('homme_de_la_semaine/(?P<id>[0-9]+)$', views.homme_de_la_semaine_show, name='homme_de_la_semaine_show'),
    path('activites/', views.activites, name='activites'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('', views.index, name='index'),
]

