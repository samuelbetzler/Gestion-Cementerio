from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('execute-scripts/', views.execute_scripts, name='execute_scripts'),
    path('success/', views.success, name='success'),
]
