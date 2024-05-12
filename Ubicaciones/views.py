from rest_framework import viewsets
from .serializer import UbicacionSerializer
from .models import Ubicacion

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
