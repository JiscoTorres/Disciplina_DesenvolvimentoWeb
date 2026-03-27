from django.shortcuts import render
from .models import Produto

# Create your views here.

def index(request):
    return render(request, 'web/index.html')

#Exercício
def sobre(request):
    return render(request, 'web/sobre.html')


def recuperar_produto(request, id):
    produto = Produto.objects.get(pk=1)
    return render(request, 'web/produto.html', {'produto': produto})

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, "web/listar_produtos.html", {'produtos':produtos})
# http://127.0.0.1:8000/teste_produto/1

#esse arquivo views.py serve para tratar a logica de negócio -> ele recebe o resultado do mapeamento feito pelas urls. 
# view model e admin são os principais dentro da pasta do aplicativo!
# Django é um framework que tem um servidor webzinho que serve para nos ajudarmos!
#servidor web recebe uma requisição na porta 8000 ai passa pra view para ela iniciar esse tratamento, ai a view vai ver o 
#<--------req:8000-----> Servirdor Web (aqui vai identificar se tem rota ou nao, identicou a rota, passa para view.py)-------------urls.py---------->  Views.py , Ai depois da requisicao, é necessário o views.py enviar uma resposta para o servidor Web,      Servidor Web <--------------.html ou json etc...----------- Views.py