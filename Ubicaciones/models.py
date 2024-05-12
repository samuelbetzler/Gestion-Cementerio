from django.db import models

class Provincia(models.Model):
    name_pro = models.TextField()

class Canton(models.Model):
    name_can = models.TextField()
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

class Ubicacion(models.Model):
    id_pro = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    id_can = models.ForeignKey(Canton, on_delete=models.CASCADE)
