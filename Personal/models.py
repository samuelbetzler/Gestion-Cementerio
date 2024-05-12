from django.db import models

class TipoPersonal(models.Model):
    name_tipo_per = models.TextField()

class Personal(models.Model):
    id_tipo_per = models.ForeignKey(TipoPersonal, on_delete=models.CASCADE)
    ci_per = models.CharField(max_length=10)
    name_per = models.TextField()
    lname_per = models.TextField()
    fch_naci_per = models.DateField()
    tel1_per = models.CharField(max_length=10)
    tel2_per = models.CharField(max_length=10)
