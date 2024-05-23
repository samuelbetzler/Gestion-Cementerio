# DBrestorer/urls.py
from django.urls import path
from .views import backup_restore, download_backup

urlpatterns = [
    path('backup-restore/', backup_restore, name='backup_restore'),
    path('download-backup/<str:file_name>/', download_backup, name='download_backup'),
]
