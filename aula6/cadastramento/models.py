from django.db import models

class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField()
    pais = models.TextField()
    estado = models.TextField()
    cidade = models.TextField()
