from rest_framework import serializers
from .models import Estructura

class EstructuraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estructura
        fields = '__all__'