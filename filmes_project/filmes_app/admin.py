from django.contrib import admin
from filmes_app.models import Filme, Genero

# Register your models here.

admin.site.register(Genero)
admin.site.register(Filme)
