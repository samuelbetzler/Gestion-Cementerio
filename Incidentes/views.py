from rest_framework import viewsets
from .serializer import ReporteIncidenteSerializer
from .models import ReporteIncidente

class ReporteIncidenteViewSet(viewsets.ModelViewSet):
    queryset = ReporteIncidente.objects.all()
    serializer_class = ReporteIncidenteSerializer
