from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('avaliacao/', views.avaliacao, name='avaliacao'),
    path('atualizar-perfil/<int:idUser>/', views.atualizarPerfil, name='atualizarPerfil'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('turmas/', views.turmas, name='turmas'),
    # path('graficos/', views.graficos, name='graficos'),
    path('forum/', views.forum, name='forum'),



    path('turmas/<int:idTurma>/projetos-turma/', views.projetosTurma, name='projetosTurma'),
    path('turmas/criar-turma/', views.criarTurma, name='criarTurma'),
    path('turmas/<int:idTurma>/criar-projeto/', views.criarProjeto, name='criarProjeto'),
    path('turmas/<int:idTurma>/editar-turma/', views.editarTurma, name='editarTurma'),
    path('turmas/<int:idTurma>/excluir-turma/', views.excluirTurma, name='excluirTurma'),
    path('turmas/participar-turma/', views.participarTurma, name='participarTurma'),

    path('turmas/<int:idTurma>/projetos-turma/<int:idProj>/excluir-projeto/', views.excluirProjeto, name='excluirProjeto'),
    path('turmas/<int:idTurma>/projetos-turma/<int:idProj>/editar-projeto/', views.editarProjeto, name='editarProjeto'),

    path('forum/enviarMensagem/', views.enviarMensagem, name='enviarMensagem'),
    path('forum/get-mensagens/', views.getMensagens, name='getMensagens'),

    path('turmas/<int:idTurma>/projetos-turma/<int:idProj>/projeto-backlog/', views.projetoBacklog, name='projetoBacklog'),
    path('turmas/<int:idTurma>/projetos-turma/<int:idProj>/projeto-sprints/', views.projetoSprints, name='projetoSprints'),
    path('turmas/<int:idTurma>/projetos-turma/<int:idProj>/projeto-alunos/', views.projetoAlunos, name='projetoAlunos'),
    path('turmas/<int:idTurma>/projetos-turma/<int:idProj>/projeto-anotacoes/', views.projetoAnotacoes, name='projetoAnotacoes'),
    path('turmas/<int:idTurma>/projetos-turma/<int:idProj>/projeto-anotacoes/salvar-anotacoes/', views.salvarAnotacoes, name='salvarAnotacoes'),
    path('turmas/<int:idTurma>/projetos-turma/<int:idProj>/projeto-alunos/<int:idUsuario>/rem-alunos/', views.revMembro, name='revMembro'),

    path('turmas/<int:idTurma>/projetos-turma/<int:idProj>/projeto-sprints/criar-sprint/', views.criarSprint, name='criarSprint'),
    path('turmas/<int:idTurma>/projetos-turma/<int:idProj>/projeto-sprints/<int:idSprint>/editar-sprint/', views.editarSprint, name='editarSprint'),
    path('turmas/<int:idTurma>/projetos-turma/<int:idProj>/projeto-sprints/<int:idSprint>/excluir-sprint/', views.excluirSprint, name='excluirSprint'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)