from django.db import models

class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150, null=False, blank=False)
    num_telefone = models.CharField(max_length=11, null=False, blank=False) # num de tel com ddd e sem . e -
    email = models.CharField(max_length=50, null=False, blank=False)



    objetos = models.Manager()