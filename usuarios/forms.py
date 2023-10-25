from django.db import models
from django import forms
from .models import Pessoa

class UserForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = [
            'nome',
            'cpf',
            'sexo',
            'data'
        ]
