from django.db import models


class Plano(models.Model):    
    nome = models.CharField(max_length=25)
    servicos = models.TextField(max_length=300)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    dependentes = models.IntegerField(default=0)
    vidas = models.ManyToManyField("vidas.Vida", related_name="planos")
