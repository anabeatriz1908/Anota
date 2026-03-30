from django.db import models
from .barbeiro import Barbeiros


class Servicos(models.Model):
    id_servico = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False, blank=False)
    descricao_servico = models.CharField(max_length=255, null=False, blank=False)
    valor = models.DecimalField(decimal_places=2, max_digits=5)

    #Chaves estrangeiras
    id_barbeiro = models.ForeignKey(Barbeiros, on_delete=models.CASCADE)


    objetos = models.Manager()
