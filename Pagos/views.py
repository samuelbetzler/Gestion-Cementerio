from rest_framework import viewsets
from .serializer import PagoSerializer
from .models import Pago

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
