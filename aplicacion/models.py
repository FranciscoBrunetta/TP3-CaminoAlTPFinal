from django.db import models

# Create your models here.
class Vinos(models.Model):
    categoria = models.CharField(max_length=50)
    varietal = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.categoria}, {self.varietal}"

class Bodegas(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}, {self.ciudad}"

class Premiados(models.Model):
    pais = models.CharField(max_length=50)
    fechaPremio = models.DateField()

    def __str__(self):
        return f"{self.pais}, {self.fechaPremio}"