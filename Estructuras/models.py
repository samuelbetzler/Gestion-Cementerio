from django.db import models

class LugarEstructura(models.Model):
    name_zona = models.TextField()
    name_manza = models.TextField()

class TipoEstructura(models.Model):
    name_tipo_estruc = models.TextField()

class EstadoEstructura(models.Model):
    name_est_estruc = models.TextField()

class Estructura(models.Model):
    id_lugar_estruc = models.ForeignKey(LugarEstructura, on_delete=models.CASCADE)
    id_tipo_estruc = models.ForeignKey(TipoEstructura, on_delete=models.CASCADE)
    id_est_estruc = models.ForeignKey(EstadoEstructura, on_delete=models.CASCADE)
    cruces = models.BooleanField()
