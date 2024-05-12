from django.urls import path, include
from rest_framework import routers
from .views import ReporteIncidenteViewSet

routers = routers.DefaultRouter()
routers.register(r'Incidentes', ReporteIncidenteViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]
    