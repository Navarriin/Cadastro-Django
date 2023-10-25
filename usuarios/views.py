from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import UserForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def cadastros(request):
    if request.method == 'GET':
        return render(request, 'novo_cadastro.html')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
        
        