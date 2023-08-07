from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="inicio"),

    path('vinos/', vinos, name="vinos"),

    path('bodegas/', bodegas, name="bodegas"),

    path('premiados/', premiados, name="premiados"),
]