from django.urls import path, include
from rest_framework import routers
from .views import DifuntoViewSet

routers = routers.DefaultRouter()
routers.register(r'difuntos', DifuntoViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]