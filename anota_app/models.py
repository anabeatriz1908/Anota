from django.db import models


# Create your models here.
# Para não deixar esse arquivo muitolongo, eu criei uma pasta chamada models com todos os models das entidades
# nesse arquivo eu importo esses models
from .Models.agendamento import Agendamento
from .Models.barbeiro import Barbeiros
from .Models.cliente import Clientes
from .Models.servicos import Servicos


