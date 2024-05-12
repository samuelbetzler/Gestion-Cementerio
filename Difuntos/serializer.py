from rest_framework import serializers
from .models import Difunto

class DifuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Difunto
        fields = '__all__'
        