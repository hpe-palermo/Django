from django.db import models

# Create your models here.
class Profile(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    bio = models.CharField(max_length=1000)
=======
    name = models.CharField(max_length=1000, blank=True)

class Mensagem(models.Model):
    remetente = models.CharField(max_length=1000, blank=True)
    texto = models.CharField(max_length=1000, blank=True)
>>>>>>> e1e9015 (first commit)
