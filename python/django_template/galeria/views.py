from django.shortcuts import render

def index(request):
    return render(request, 'sobre-mim/index.html')

def imagem(request):
    return render(request, 'sobre-mim/imagem.html')