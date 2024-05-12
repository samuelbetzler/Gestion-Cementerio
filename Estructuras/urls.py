from django.urls import path,include
from rest_framework import routers
from .views import EstructuraViewSet

routers = routers.DefaultRouter()
routers.register(r'Estructuras', EstructuraViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]