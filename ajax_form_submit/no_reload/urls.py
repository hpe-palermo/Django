from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('getProfiles', views.getProfiles, name='getProfiles'),
=======
    path('getMensagens', views.getMensagens, name='getMensagens'),
    path('sendMensagens', views.sendMensagens, name='sendMensagens'),
>>>>>>> e1e9015 (first commit)
    path('create', views.create, name='create'),
]
