"""

Esse arquivo identifica as rotas, e determina o que deve ir pra cada rota!
-> tudo que for link, tem que ser configurado em urls.py

-> tem urls.py do aplicativo criado e um outro urls.py do projeto!
-> urls.py do aplicativo não é criado automaticamente, temos que criar!







URL configuration for AulaWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path #adicionei a função include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Web.urls')), #adicionei essa linha
]
