from django.db import models
from django.contrib.auth.models import User
    
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagemPerfil = models.FileField(upload_to="img", blank=True, null=True)

    def __str__(self):
        return self.user.username
    
class Turma(models.Model):
    id = models.AutoField(primary_key=True)
    criador = models.CharField(max_length=30, blank=True, null=True)
    nome = models.CharField(max_length=20, blank=True, null=True)
    codigo = models.CharField(max_length=8, blank=True, null=True)
    alunos = models.ManyToManyField(Usuario, blank=True, null=True)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20)
    anotacoes = models.TextField(max_length=600, blank=True, null=True, default="Este projeto não possui descrição")
    turma = models.ForeignKey(Turma, blank=True, null=True, on_delete=models.CASCADE)
    membros = models.ManyToManyField(Usuario, blank=True, null=True)

    def __str__(self):
        return self.nome

class MensagemForum(models.Model):
    id = models.AutoField(primary_key=True)
    remetente = models.CharField(max_length=100, blank=True, null=True)
    imagemPerfil = models.FileField(upload_to="img", blank=True, null=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.remetente}:{self.descricao}"

class Sprint(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, blank=True, null=True, default="Sprint")
    projeto = models.ForeignKey(Projeto, blank=True, null=True, on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, blank=True, null=True, on_delete=models.CASCADE)
    dataInicio = models.DateField(auto_now_add=True, blank=True, null=True)
    dataEntrega = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, default="Criada")

    def __str__(self):
        return self.nome