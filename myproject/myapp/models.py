from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.nome

"""
{
    "id": 1,
    "nome": "Frutas"
},
{
    "id": 2,
    "nome": "Eletrônico"
}
{
    "id": 1,
    "nome": "HeadFone",
    "descricao": "fone.",
    "preco": "100.00",
    "categoria": 2
}
{
    "id": 2,
    "nome": "XBox",
    "descricao": "Videogame",
    "preco": "2000.00",
    "categoria": 2
}
{
    "id": 3,
    "nome": "Pera",
    "descricao": "Pera",
    "preco": "2.00",
    "categoria": 1
}
"""