from django.urls import path, include
from rest_framework import routers
from .views import PagoViewSet

routers = routers.DefaultRouter()
routers.register(r'Pagos', PagoViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]