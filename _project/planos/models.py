from django.db import models
import uuid


class Plano(models.Model):

    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    nome = models.CharField(max_length=25)
    servicos = models.TextField(max_length=300)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    dependentes = models.IntegerField(default=0)
    vidas = models.ManyToManyField("vidas.Vida", related_name="planos")
