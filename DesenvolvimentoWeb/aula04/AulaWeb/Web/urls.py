# inicio/urls.py
from django.urls import path
from . import views


urlpatterns = [ #isso aqui é uma lista de rotas
path('', views.index, name='index'),
]

#Exercício
urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
]