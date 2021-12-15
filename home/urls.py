from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    url('the_crew/member/(?P<id>[0-9]+)$', views.crew_member, name='member'),
    url('podcast/(?P<id>[0-9]+)$', views.podcastshow, name='podcastshow'),
    path('podcast/', views.podcast, name='podcast'),
    path('the_crew/', views.the_crew, name='crew'),
    path('games/', views.games, name='games'),
    path('explore/', views.explore, name='explore'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    url('(?P<id>[0-9]+)$', views.showpost, name='showpost'),
    path('', views.index, name='index'),
]

