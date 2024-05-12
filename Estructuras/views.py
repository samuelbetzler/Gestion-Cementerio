from rest_framework import viewsets
from .serializer import EstructuraSerializer
from .models import Estructura

class EstructuraViewSet(viewsets.ModelViewSet):
    queryset = Estructura.objects.all()
    serializer_class = EstructuraSerializer
    