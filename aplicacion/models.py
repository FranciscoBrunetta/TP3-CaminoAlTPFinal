from django.db import models

# Create your models here.
class Vinos(models.Model):
    categoria = models.CharField(max_length=50)
    varietal = models.CharField(max_length=50)

class Bodegas(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)

class Premiados(models.Model):
    pais = models.CharField(max_length=50)
    fechaPremio = models.DateField()