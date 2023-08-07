from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

def vinos(request):
    ctx = {"vinos": Vinos.objects.all()}
    return render(request, "aplicacion/vinos.html",ctx)

def vinosForm(request):
    if request.method == "POST":
        vino = Vinos(categoria=request.POST['categoria'], varietal=request.POST['varietal'])
        vino.save()
        return HttpResponse("Se ingreso con exito el vino!")
    return render(request, "aplicacion/vinosForm.html")

def vinosForm2(request):
    if request.method == "POST":
        miForm = VinoForm(request.POST)
        print(miForm)
        if miForm.is_valid:
            informacion = miForm.cleaned_data
            vino = Vinos(categoria=informacion['categoria'], varietal=informacion['varietal'])
            vino.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm =VinoForm()
    return render(request, "aplicacion/vinosForm2.html", {"form" :miForm})

def buscarCategoria(request):
    return render(request, "aplicacion/buscarCategoria.html")

def buscar2(request):
    if request.GET['categoria']:
        categoria = request.GET['categoria']
        vinos = Vinos.objects.filter(categoria__icontains=categoria)
        return render(request, "aplicacion/resultadosCategoria.html", {"categoria":categoria, "vino": vinos})

def bodegas(request):
    return render(request, "aplicacion/bodegas.html")

def premiados(request):
    return render(request, "aplicacion/premiados.html")
