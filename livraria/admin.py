from django.contrib import admin

from .models import Categoria, Editora, Autor


admin.site.register(Editora)
admin.site.register(Categoria)
admin.site.register(Autor)