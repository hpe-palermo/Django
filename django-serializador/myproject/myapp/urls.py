from django.urls import path
from .views import AuthorListCreate, AuthorDetail, BookListCreate, BookDetail

urlpatterns = [
    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]
