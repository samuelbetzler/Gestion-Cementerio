from django.urls import path
from . import views

app_name = 'sqlscripts'

urlpatterns = [
    path('', views.index, name='index'),
    path('execute/', views.execute_scripts, name='execute_scripts'),
    path('success/', views.success, name='success'),
]
