from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.descricao} ({self.id})"

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    site = models.URLField(null=True, blank=True)#esse campo e opcional

    def __str__(self):
        return self.nome
    
class Autor(models.Model):
    nome = models.CharField(max_length=225)
    email = models.EmailField(null=True, blank=True)  

    def __str__(self):
        return self.nome   
    
    class Meta:
        verbose_name_plural = "Autores"

class Livro(models.Model):
    nome = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255 , null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2 , default=0, null=True, blank= True)
    categoria = models.ForeignKey( Categoria, on_delete=models.PROTECT, related_name="livros")
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros")
    autores = models.ManyToManyField(Autor, related_name="livros")

    def __str__(self):
        return f"{self.nome}({self.quantidade})"

