from django.urls import path, include
from rest_framework import routers
from .views import PersonalViewSet

routers = routers.DefaultRouter()
routers.register(r'Personal', PersonalViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]