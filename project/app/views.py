from django.shortcuts import render
from PIL import Image
import os
from django.conf import settings
from .models import MyFile

# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    elif request.method == 'POST':
        
        # recuperar a imagem
        file = request.FILES.get("my_file")

        """
         
        img = Image.open(file)

        # onde vai salvar?
        # media/NOME_DO_ARQUIVO.EXTENSAO
        # a extensao tem que ser a mesma que ele aceita
        path = os.path.join(settings.BASE_DIR, f'media/{file.name}.png')
        img = img.save(path)
        

        -> pesquisar por NGINX, proxy reverse, definir tamanho da requisição

        propriedades file (File Object)
        file.
            name, size, file( instancia de BytesIO )

            for b in file.file:
                print(b)

            este for terá que percorrer todo o arquivo 

            for b in file.chunks():
                print(b)
            com file.chunk(), ele fornece conforme é solicitado
            pede 64, usa , pede mais 64, usa , etc
            
        """
        

        # if file.size > 20000000:
            # return erro
        
        # salvar no banco
        mf = MyFile(title="minha_imagem", arq=file)
        mf.save()

        return render(request, 'imagem.html')