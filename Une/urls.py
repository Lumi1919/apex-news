from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'Une'
urlpatterns = [
    path('', views.index, name='index'),
]