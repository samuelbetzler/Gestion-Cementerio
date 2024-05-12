from django.contrib import admin
from .models import Provincia, Canton, Ubicacion

# Register your models here.
admin.site.register(Provincia)
admin.site.register(Canton)
admin.site.register(Ubicacion)