from django.db import models
import uuid


class Sexo(models.TextChoices):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"
    DEFAULT = "Not Informed"


class Integracao(models.TextChoices):
    PENDENTE = "Pendente"
    INTEGRADO = "Integrado"
    REVISAR = "Revisar"


class Vida(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=120)
    idade = models.IntegerField()
    sexo = models.CharField(choices=Sexo.choices, default=Sexo.DEFAULT, max_length=25)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    data_de_criacao = models.DateTimeField(auto_now_add=True)
    integracao = models.CharField(choices=Integracao.choices, default=Integracao.PENDENTE)
