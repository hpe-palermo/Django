from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('produtos/', ProdutoListCreateAPIView.as_view(), name='produto-list-create'),
    path('produtos/<int:id>/', ProdutoListCreateAPIView.as_view(), name='produto-list-one'),
    path('categorias/', CategoriaListCreateAPIView.as_view(), name='categoria-list-create'),
    path('produtos/categoria/<int:id>', ProdutoCategoriaListAPIView.as_view(), name='produto-categoria-list'),
]
