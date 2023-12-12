from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from random import randint, choice
from .models import *
# from DateTime import DateTime

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'credenciais/cadastro.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password = request.POST['password']
        user = User.objects.filter(username=username).first()
        if user:
            return render(request, "credenciais/cadastro.html", { "erro": "Já existe um usuário com este username!"})
        user = User.objects.create(username=username, email=email, password=make_password(password))
        user.save()

        userMaisCampos = Usuario(
            user = user,
        )
        userMaisCampos.save()

        return redirect("/login/")

def login(request):
    if request.method == 'GET':
        return render(request, 'credenciais/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password) or authenticate(email=username, password=password)
        if user:
            login_django(request, user)
            return redirect("/dashboard/")
        else:
            return render(request, "credenciais/login.html", { "erro": "Credenciais incorretas!"})

def avaliacao(request):
    nomeAvaliacao = request.POST.get("nomeAvaliacao")
    mensagem = request.POST.get("mensagem")
    texto = f"Usuário: {nomeAvaliacao}\n\n" + mensagem
    email = "planningtasks2023@gmail.com"
    send_mail(
            "AVALIAÇÃO",
            texto,
            email,
            recipient_list=[email]
        )
    print("Enviado")
    return redirect('/')

#=======================================================================================

@login_required(login_url="/login/")
def dashboard(request):
    dados = {
        "nomePagina": "Dashboard",
        "usuario": Usuario.objects.get(user=request.user)
    }
    return render(request, 'corpo/dashboard.html', dados)

def excluirConta(request, nomeUser):
    user = User.objects.get(username=nomeUser)
    usuario = Usuario.objects.get(user=user)
    usuario.delete()
    return redirect('/login/')

def atualizarPerfil(request, idUser):
    usuario = User.objects.get(id=idUser)
    usuario.username = request.POST['username']
    usuario.save()
    
    usuarioImg = Usuario.objects.get(user=usuario)
    if request.POST['excluirFotoPerfil'] == "nao":
        url_imagem = request.FILES.get('imagem')
        if url_imagem:
            usuarioImg.imagemPerfil = url_imagem
        usuarioImg.save()
    else:
        usuarioImg.imagemPerfil = None
        usuarioImg.save()
    return redirect('/dashboard/')

@login_required(login_url="/login/")
def sair(request):
    logout(request)
    return redirect("/login/")

@login_required(login_url="/login/")
def turmas(request):
    usuario = Usuario.objects.get(user=request.user)
    listaTurmas = []
    for t in Turma.objects.all():
        if usuario in t.alunos.all() or usuario.user.username == t.criador:
            listaTurmas.append(t)

    dados = {
        "nomePagina": "Turmas",
        "usuario": Usuario.objects.get(user=request.user),
        "turmas": listaTurmas
    }
    return render(request, 'corpo/turmas.html', dados)

def codigoTurma():
    letras = [chr(letra) for letra in range(65,91)]
    letras += [chr(letra) for letra in range(97,123)]
    code_letters = [choice(letras) for l in range(5)]
    return f'{code_letters[0]}{randint(0,9)}{"".join(code_letters[1:])}{randint(0,9)}'

def participarTurma(request):
    if Turma.objects.filter(codigo=request.POST.get('codigo')).first():
        turma = Turma.objects.filter(codigo=request.POST.get('codigo')).first()
        print("turma:",turma)
        usuario = Usuario.objects.get(user=request.user)
        turma.alunos.add(usuario)
        turma.save()
    return redirect("/turmas/")

def criarTurma(request):
    nome = request.POST.get('nome')
    usuario = Usuario.objects.get(user=request.user)
    if nome:
        if len(Turma.objects.filter(nome=nome, criador=request.user.username)) == 0:
            turma = Turma(
                criador = request.user.username,
                nome = nome,
                codigo = codigoTurma(),
            )
            turma.save()
            turma.alunos.add(usuario)
            turma.save()
        return redirect('/turmas')

def criarProjeto(request, idTurma):
    turma = Turma.objects.get(id=idTurma)
    nome = request.POST.get('nome')
    usuario = Usuario.objects.get(user=request.user)

    if nome:
        if len(Projeto.objects.filter(nome=nome, turma=turma)) == 0:
            projeto = Turma(
                nome = nome,
                turma = turma
            )
            projeto.save()
    return redirect(f"/turmas/{idTurma}/projetos-turma/")

def editarTurma(request, idT):
    turma = Turma.objects.get(id=idT)
    turma.nome = request.POST.get(f'nomeEditado{idT}')
    turma.save()
    return redirect("/turmas/")

def excluirTurma(request, idT):
    turma = Turma.objects.get(id=idT)
    turma.delete()
    return redirect("/turmas")

def projetosTurma(request, idTurma):
    turma = Turma.objects.get(id=idTurma)
    usuario = Usuario.objects.get(user=request.user)
    projetos = []

    for p in Projeto.objects.filter(turma=turma):
        if (turma.criador == usuario.user.username) or (usuario in p.membros.all()):
            projetos.append(p)

    dados = {
        "nomePagina": "Turmas",
        "usuario": Usuario.objects.get(user=request.user),
        "turma": turma,
        "projetos": projetos
    }
    return render(request, 'corpo/projetos-turma.html', dados)

def editarProjeto(request, idTurma, idProj):
    projeto = Projeto.objects.get(id=idProj)
    projeto.nome = request.POST.get(f'nomeEditado{idProj}')
    projeto.save()
    return redirect(f"/turmas/{idTurma}/projetos-turma/")

def excluirProjeto(request, idTurma, idProj):
    projeto = Projeto.objects.get(id=idProj)
    projeto.delete()
    return redirect(f"/turmas/{idTurma}/projetos-turma/")

def forum(request):
    dados = {
        "usuario": Usuario.objects.get(user=request.user),
        "mensagensForum": MensagemForum.objects.all(),
        "nomePagina": "Fórum"
    }
    return render(request, 'corpo/forum.html', dados)

def enviarMensagem(request):
    mensagemForum = MensagemForum(
        remetente = request.user.username,
        imagemPerfil = Usuario.objects.get(user=request.user).imagemPerfil,
        descricao = request.POST.get('mensagemForum')
    )
    mensagemForum.save()
    return HttpResponse("ok")

def getMensagens(request):
    return JsonResponse({ "mensagensForum" : list(MensagemForum.objects.all().values()) })

def projetoBacklog(request, idTurma, idProj):
    turma = Turma.objects.get(id=idTurma)
    projeto = Projeto.objects.get(id=idProj)
    dados = {
        "usuario": Usuario.objects.get(user=request.user),
        "nomePagina": f"Projetos:{projeto.nome}",
        "projeto": projeto,
        "turma": turma,
        # "tarefas": tarefas
    }
    return render(request, 'corpo/projeto-backlog.html', dados)

def projetoSprints(request, idTurma, idProj):
    turma = Turma.objects.get(id=idTurma)
    projeto = Projeto.objects.get(id=idProj)
    dados = {
        "usuario": Usuario.objects.get(user=request.user),
        "nomePagina": f"Projetos:{projeto.nome}",
        "projeto": projeto,
        "turma": turma,
        "sprints": Sprint.objects.filter(turma=turma, projeto=projeto)
    }
    return render(request, 'corpo/projeto-sprints.html', dados)

def projetoAlunos(request, idTurma, idProj):
    turma = Turma.objects.get(id=idTurma)
    projeto = Projeto.objects.get(id=idProj)
    dados = {
        "usuario": Usuario.objects.get(user=request.user),
        "nomePagina": f"Projetos:{projeto.nome}",
        "projeto": projeto,
        "turma": turma,
        "alunos": projeto.membros.all()
    }
    return render(request, 'corpo/projeto-alunos.html', dados)

def projetoAnotacoes(request, idTurma, idProj):
    turma = Turma.objects.get(id=idTurma)
    projeto = Projeto.objects.get(id=idProj)
    dados = {
        "usuario": Usuario.objects.get(user=request.user),
        "nomePagina": f"Projetos:{projeto.nome}",
        "projeto": projeto,
        "turma": turma,
        # "anotacoes": anotacoes
    }
    return render(request, 'corpo/projeto-anotacoes.html', dados)

def salvarAnotacoes(request, idTurma, idProj):
    projeto = Projeto.objects.get(id=idProj)
    anotacoes = request.POST.get('anotacoes')
    if anotacoes == None:
        print("================================================")
        anotacoes = "Este projeto não possui descrição"
    print('f1')
    projeto.anotacoes = anotacoes
    print('f2')
    projeto.save()
    print('f3')
    return redirect(f'/turmas/{idTurma}/projetos-turma/{idProj}/projeto-anotacoes/')

def revMembro(request, idTurma, idProj, idUsuario):
    usuario = Usuario.objects.get(id=idUsuario)
    projeto = Projeto.objects.get(id=idProj)
    projeto.membros.remove(usuario)
    projeto.save()
    return redirect(f'/turmas/{idTurma}/projetos-turma/{idProj}/projeto-alunos/')

def criarSprint(request, idTurma, idProj):
    nome = request.POST.get('nome')
    if nome:
        dataInicio = request.POST.get('dataInicio')
        dataEntrega = request.POST.get('dataEntrega')
        if Sprint.objects.filter(nome=nome).count() == 0:
            sprint = Sprint(
                nome = nome,
                turma = Turma.objects.get(id=idTurma),
                projeto = Projeto.objects.get(id=idProj),
                dataInicio = dataInicio,
                dataEntrega = dataEntrega
            )
            sprint.save()
    return redirect(f'/turmas/{idTurma}/projetos-turma/{idProj}/projeto-sprints/')

def editarSprint(request, idTurma, idProj, idSprint):
    sprint = Sprint.objects.get(id=idProj)
    sprint.nome = request.POST.get('nome')
    sprint.save()
    return redirect(f'/turmas/{idTurma}/projetos-turma/{idProj}/projeto-sprints/')

def excluirSprint(request, idTurma, idProj, idSprint):
    sprint = Sprint.objects.get(id=idProj)
    sprint.delete()
    return redirect(f'/turmas/{idTurma}/projetos-turma/{idProj}/projeto-sprints/')