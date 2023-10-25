from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import UserForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def cadastros(request):
    """funçao de cadastrar usuario"""
    if request.method == 'GET':
        return render(request, 'novo_cadastro.html')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return usuarios(request)

def usuarios(request):
    variaveis = Pessoa.objects.all()
    context = {'variaveis': variaveis}
    return render(request, 'usuarios.html', context)
        
        