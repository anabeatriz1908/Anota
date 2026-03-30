from django.db import models
from .barbeiro import Barbeiros
from .cliente import Clientes
from .servicos import Servicos


class Agendamento(models.Model):
    id_agendamento = models.AutoField(primary_key=True)
    data_hora_agendamento = models.DateTimeField()

    # Chaves estrangeiras
    id_barbeiro = models.ForeignKey(Barbeiros, on_delete=models.CASCADE)
    id_cleinte = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    
    valor_total = models.DecimalField(decimal_places=2, max_digits=5, default=0.0)



    objetos = models.Manager()