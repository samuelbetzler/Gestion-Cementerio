from django.urls import path, include
from rest_framework import routers
from .views import ClienteViewSet

routers = routers.DefaultRouter()
routers.register(r'clientes', ClienteViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]