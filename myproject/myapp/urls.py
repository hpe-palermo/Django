from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('produtos/', ProdutoListCreateAPIView.as_view(), name='produto-list-create'),
    path('categorias/', CategoriaListCreateAPIView.as_view(), name='categoria-list-create'),
]
