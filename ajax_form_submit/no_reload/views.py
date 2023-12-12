from django.shortcuts import render
from .models import Profile
from .models import *
from django.http import JsonResponse, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def getProfiles(request):
    profiles = Profile.objects.all()
    return JsonResponse({"profiles": list(profiles.values())})

    return render(request, 'inserirNome.html')

def getMensagens(request):
    mensagens = Mensagem.objects.all()
    return JsonResponse({"mensagens": list(mensagens.values())})

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        bio = request.POST['bio']
        new_profile = Profile(name=name, email=email, bio=bio)
        new_profile.save()

        return HttpResponse('New Profile Created Successfully')


        new_profile = Profile(name=name)
        new_profile.save()

        return render(request, 'chat.html', {'new_profile': new_profile})

def sendMensagens(request):
    if request.method == 'POST':
        name = request.POST['name']
        msg = request.POST['msg']
        new_message = Mensagem(remetente=name, texto=msg)
        new_message.save()
        
        return HttpResponse('Message send Successfully')
