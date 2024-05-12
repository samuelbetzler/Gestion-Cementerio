from django.db import models
from Clientes.models import Tramite  

class Certificado(models.Model):
    id_tram = models.ForeignKey(Tramite, on_delete=models.CASCADE)

