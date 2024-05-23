# DBrestorer/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from .forms import BackupRestoreForm
import os
from django.conf import settings
import glob

def backup_restore(request):
    backup_file_name = None

    if request.method == 'POST':
        form = BackupRestoreForm(request.POST, request.FILES)
        if form.is_valid():
            action = form.cleaned_data['action']
            if action == 'backup':
                os.system('python manage.py dbbackup')
                backup_files = sorted(glob.glob(str(settings.BASE_DIR / 'backup' / '*.backup')), key=os.path.getmtime, reverse=True)
                if backup_files:
                    backup_file_path = backup_files[0]
                    backup_file_name = os.path.basename(backup_file_path)
                return render(request, 'DBrestorer/backup_restore.html', {'form': form, 'backup_file': backup_file_name})
            elif action == 'restore' and 'file' in request.FILES:
                file = request.FILES['file']
                file_path = os.path.join(settings.BASE_DIR, 'backup', file.name)
                with open(file_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                os.system(f'python manage.py dbrestore --input {file_path}')
                return HttpResponse('Restore completed successfully.')
    else:
        form = BackupRestoreForm()

    return render(request, 'DBrestorer/backup_restore.html', {'form': form, 'backup_file': backup_file_name})

def download_backup(request, file_name):
    file_path = os.path.join(settings.BASE_DIR, 'backup', file_name)
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
    else:
        return HttpResponse('File not found.', status=404)
