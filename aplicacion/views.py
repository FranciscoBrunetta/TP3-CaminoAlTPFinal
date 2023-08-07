from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

def vinos(request):
    ctx = {"categoria": "Tinto", "varietal": "Malbec"}
    return render(request, "aplicacion/vinos.html",ctx)

def bodegas(request):
    return render(request, "aplicacion/bodegas.html")

def premiados(request):
    return render(request, "aplicacion/premiados.html")
