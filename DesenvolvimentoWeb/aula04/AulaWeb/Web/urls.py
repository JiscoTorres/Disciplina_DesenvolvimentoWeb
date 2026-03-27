# inicio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre/', views.sobre, name='sobre'),
    path('teste_produto/<int:id>', views.recuperar_produto, name='teste'),
    path('listar_produto', views.listar_produtos, name='listar_produtos')
]