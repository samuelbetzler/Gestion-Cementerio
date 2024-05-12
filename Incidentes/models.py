from django.db import models
from Personal.models import    Personal

class TipoIncidente(models.Model):
    name_tipo_inci = models.CharField(max_length=30)

class ReporteIncidente(models.Model):
    id_tipo_inci = models.ForeignKey(TipoIncidente, on_delete=models.CASCADE)
    id_per = models.ForeignKey(Personal, on_delete=models.CASCADE)
    fch_rep_inc = models.DateField()
  
