from django.urls import path, include
from rest_framework import routers
from .views import UbicacionViewSet

routers = routers.DefaultRouter()
routers.register(r'Ubicaciones', UbicacionViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]