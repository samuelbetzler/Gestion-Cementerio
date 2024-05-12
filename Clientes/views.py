from rest_framework import viewsets
from .serializer import ClienteSerializer
from .models import Cliente

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


