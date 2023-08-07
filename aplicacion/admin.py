from django.contrib import admin
from .models import Vinos, Bodegas, Premiados

# Register your models here.
admin.site.register(Vinos)
admin.site.register(Bodegas)
admin.site.register(Premiados)
