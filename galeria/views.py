from django.shortcuts import render

# Create your views here.

dados = {
    1: {'nome': 'Nebulosa de Carina',
        'legenda': 'webbtelescope.org / Nasa / James Webb'},
    2: {'nome': 'Galáxia NGC 1079',
        'legenda': 'nasa.org / Nasa / Hubble'}
}

def index(request):
    return render(request,
                  'galeria/index.html',
                  {'cards': dados})

def imagem(request):
    return render(request,
                  'galeria/imagem.html')