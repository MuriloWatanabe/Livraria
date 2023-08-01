from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from livraria.models import Categoria, Editora, Autor , Livro
from livraria.serializers import CategoriaSerializer , EditoraSerializer, AutorSerializer, LivroSerializer, LivroDetailSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return LivroDetailSerializer
        return LivroSerializer    