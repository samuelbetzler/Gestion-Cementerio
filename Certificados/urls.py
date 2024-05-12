from django.urls import path, include
from rest_framework import routers
from .views import CertificadoViewSet

routers = routers.DefaultRouter()
routers.register(r'certificados', CertificadoViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]