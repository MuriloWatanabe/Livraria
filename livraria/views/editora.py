from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from livraria.models import Categoria, Editora, Autor , Livro
from livraria.serializers import CategoriaSerializer , EditoraSerializer, AutorSerializer, LivroSerializer, LivroDetailSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer