from django.db import models

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    
