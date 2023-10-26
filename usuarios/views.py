from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import UserForm
# Create your views here.

def index(request):
    """renderiza a pagina inicial"""
    return render(request, 'index.html')

def cadastros(request): # CREATE/POST
    """funçao de cadastrar usuario"""
    form = UserForm()
    context = {'form': form}
    if request.method == 'GET':
        if form.is_valid():
            return render(request, 'novo_cadastro.html', context)
        else:
            return render(request, 'novo_cadastro.html')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return usuarios(request)
        return render(request, 'novo_cadastro.html', context)
       

def usuarios(request): # READ/GET
    """funçao que mostra todos os usuarios cadastrados"""
    variaveis = Pessoa.objects.all()
    context = {'variaveis': variaveis}
    return render(request, 'usuarios.html', context)
        
def deletar(request, usuarios_id): # DELETE
    """funçao para deletar usuario"""
    variavel = Pessoa.objects.get(id=usuarios_id)
    variavel.delete()
    return redirect('/usuarios/')

def atualizar(request, usuario_id): # UPDATE/POP
    """funçao que deleta o usuario por id e cria um novo (atualiza)"""
    variavel = Pessoa.objects.get(id=usuario_id)
    context = {'variavel': variavel}
    if request.method == 'GET':
        return render(request, 'atualizar.html', context)
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            variavel.delete()
            return redirect('/usuarios/')
        else:
            return error(request)
    
def error(request):
    return render(request, 'error.html')
