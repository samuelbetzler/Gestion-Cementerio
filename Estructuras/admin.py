from django.contrib import admin
from django.contrib import admin
from .models import LugarEstructura, TipoEstructura, EstadoEstructura, Estructura


admin.site.register(LugarEstructura)
admin.site.register(TipoEstructura)
admin.site.register(EstadoEstructura)
admin.site.register(Estructura)