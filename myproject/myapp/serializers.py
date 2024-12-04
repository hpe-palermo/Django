from rest_framework import serializers
from .models import *   

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__' # ou defina campos específicos: ['id', 'nome', 'descricao', 'preco']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__' 