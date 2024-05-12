from django.db import models

class CausaMuerte(models.Model):
    name_cau_mue = models.TextField()

class Difunto(models.Model):
    id_cau_mue = models.ForeignKey(CausaMuerte, on_delete=models.CASCADE)
    name_difu = models.TextField()
    lastn_difu = models.TextField()
    fch_naci_difu = models.DateField()
    fch_muerte_difu = models.DateField()
    code_acta_difu = models.CharField(max_length=5)
