from django.db import models
from Clientes.models import Cliente,Tramite



class TipoPago(models.Model):
    name_tipo_pago = models.TextField()

class Pago(models.Model):
    id_tipo_pago = models.ForeignKey(TipoPago, on_delete=models.CASCADE)
    id_tram = models.ForeignKey(Tramite, on_delete=models.CASCADE)
    cant_pago = models.DecimalField(max_digits=6, decimal_places=2)
    fch_pago = models.DateField()

