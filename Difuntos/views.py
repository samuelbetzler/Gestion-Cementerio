from rest_framework import viewsets
from .serializer import DifuntoSerializer
from .models import Difunto

class DifuntoViewSet(viewsets.ModelViewSet):
    queryset = Difunto.objects.all()
    serializer_class = DifuntoSerializer
