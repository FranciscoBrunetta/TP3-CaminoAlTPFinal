from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="inicio"),

    path('vinos/', vinos, name="vinos"),
    path('bodegas/', bodegas, name="bodegas"),
    path('premiados/', premiados, name="premiados"),

    path('vino_form/', vinosForm, name="vino_form"),
    path('vino_form2/', vinosForm2, name="vino_form2"),

    path('buscar_categoria/', buscarCategoria, name="buscar_categoria"),
    path('buscar2/', buscar2, name="buscar2"),

]