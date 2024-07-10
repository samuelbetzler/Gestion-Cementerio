from django.urls import path
from . import views

urlpatterns = [
    path('generar-informe/', views.generar_informe, name='generar_informe'),
    path('listar-auditoria/', views.listar_auditoria, name='listar_auditoria'),
    path('listar-consultas/', views.listar_consultas, name='listar_consultas'),
    path('ejecutar-consulta/', views.ejecutar_consulta, name='ejecutar_consulta'),
    path('comparacion-hilos/', views.comparacion_hilos, name='comparacion_hilos'),
]
