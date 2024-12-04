from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo à API! Acesse /produtos/ para listar ou criar produtos.")
    
class ProdutoListCreateAPIView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                produto = Produto.objects.get(id=id)
                serializer = ProdutoSerializer(produto)
                return Response(serializer.data)
            except Produto.DoesNotExist:
                return Response({"error": "Produto não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            produtos = Produto.objects.all()
            serializer = ProdutoSerializer(produtos, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            produto = Produto.objects.get(id=id)
        except Produto.DoesNotExist:
            return Response({"error": "Produto não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProdutoSerializer(produto, data=request.data, partial=True)  # `partial=True` permite atualizações parciais
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            produto = Produto.objects.get(id=id)
            produto.delete()
            return Response({"message": "Produto excluído com sucesso"}, status=status.HTTP_204_NO_CONTENT)
        except Produto.DoesNotExist:
            return Response({"error": "Produto não encontrado"}, status=status.HTTP_404_NOT_FOUND)


class CategoriaListCreateAPIView(APIView):
    def get(self, request, id=None):
        if id:
            try:
                categoria = Categoria.objects.get(id=id)
                serializer = CategoriaSerializer(categoria)
                return Response(serializer.data)
            except Categoria.DoesNotExist:
                return Response({"error": "Categoria não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        else:
            produtos = Produto.objects.all()
            serializer = ProdutoSerializer(produtos, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        try:
            categoria = Categoria.objects.get(id=id)
        except Categoria.DoesNotExist:
            return Response({"error": "Categoria não encontrada"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CategoriaSerializer(categoria, data=request.data, partial=False)  # `partial=False` significa que todos os campos precisam ser enviados
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        try:
            categoria = Categoria.objects.get(id=id)
            categoria.delete()
            return Response({"message": "Categoria excluída com sucesso"}, status=status.HTTP_204_NO_CONTENT)
        except Categoria.DoesNotExist:
            return Response({"error": "Categoria não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    
class ProdutoCategoriaListAPIView(ListAPIView):
    serializer_class = ProdutoSerializer

    def get_queryset(self):
        categoria_id = self.kwargs['id']  # Captura o ID da categoria da URL
        return Produto.objects.filter(categoria=categoria_id)

        