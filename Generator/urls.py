from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('generar_reporte/', views.generar_reporte, name='generar_reporte'),
]
