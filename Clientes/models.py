from django.db import models
from Difuntos.models import Difunto
from Ubicaciones.models import Ubicacion


class Cliente(models.Model):
    id_ubi = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)  
    ci_clien = models.CharField(max_length=10)
    name_clien = models.TextField()
    lname_clien = models.TextField()
    fch_naci_clien = models.DateField()
    tel1_clien = models.CharField(max_length=10)
    tel2_clien = models.CharField(max_length=10)
    
class Tramite(models.Model):
    id_clien = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_difu = models.ForeignKey(Difunto, on_delete=models.CASCADE)
