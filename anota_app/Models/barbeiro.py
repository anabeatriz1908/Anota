from django.db import models

class Barbeiros(models.Model):
    id_barbeiro = models.AutoField(primary_key=True)
    # Barbeiro tem outros atributos e metodos, depois quem ficou responsavel por essa parte adiciona o restante aqui


    objetos = models.Manager()