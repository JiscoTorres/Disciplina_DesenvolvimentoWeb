from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'Web/index.html')

#Exercício
def sobre(request):
    return render(request, 'Web/sobre.html')


#esse arquivo views.py serve para tratar a logica de negócio -> ele recebe o resultado do mapeamento feito pelas urls. 
# view model e admin são os principais dentro da pasta do aplicativo!
# Django é um framework que tem um servidor webzinho que serve para nos ajudarmos!
#servidor web recebe uma requisição na porta 8000 ai passa pra view para ela iniciar esse tratamento, ai a view vai ver o 
#<--------req:8000-----> Servirdor Web (aqui vai identificar se tem rota ou nao, identicou a rota, passa para view.py)-------------urls.py---------->  Views.py , Ai depois da requisicao, é necessário o views.py enviar uma resposta para o servidor Web,      Servidor Web <--------------.html ou json etc...----------- Views.py