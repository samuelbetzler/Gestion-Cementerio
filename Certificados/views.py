from rest_framework import viewsets
from .serializer import CertificadoSerializer
from .models import Certificado

class CertificadoViewSet(viewsets.ModelViewSet):
    queryset = Certificado.objects.all()
    serializer_class = CertificadoSerializer

