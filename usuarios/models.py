from django.db import models

# Create your models here.

    
class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    data = models.DateField(null=False)

    def __str__(self):
        return self.nome