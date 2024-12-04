from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__' # ou defina campos específicos: ['id', 'nome', 'descricao', 'preco']
