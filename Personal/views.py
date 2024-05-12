from rest_framework import viewsets
from .serializer import PersonalSerializer
from .models import Personal

class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
