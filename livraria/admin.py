from django.contrib import admin

from .models import Categoria, Editora


admin.site.register(Editora)
admin.site.register(Categoria)