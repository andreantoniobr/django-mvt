from django.shortcuts import render
from .models import Filme

def lista_filmes(request):
    filmes = Filme.objects.order_by("-ano_lancamento")
    return render(request, 'filmes/lista.html', {'filmes': filmes})
