from django.shortcuts import render
from .models import Usuario

def home(resquest):# criada um função para fazer resquest home
    return render(resquest,'usuarios/home.html') # onde vai retornar resquest da página HTML

# Create your views here.

# salvar os dados da tela no banco de dados 
def usuarios(resquest):
    novo_usuario = Usuario()
    novo_usuario.nome = resquest.POST.get('nome')
    novo_usuario.idade = resquest.POST.get('idade')
    novo_usuario.save()
    # exibir os dados cadastrados em uma nova página 
    # antes de buscar no mbanco de dados, precisa criar um dicionario no python 
    usuarios = {
     'usuarios': Usuario.objects.all() # 'usuario é a chave d dicionario Usuario.objects.all() é onde vai buscar no banco de dados '
    }

    # Retornar os dados para página de listagem de usuarios 

    return render(resquest,'usuarios/usuarios.html',usuarios)