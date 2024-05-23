from django import forms

class BackupRestoreForm(forms.Form):
    BACKUP_CHOICES = [
        ('backup', 'Backup'),
        ('restore', 'Restore'),
    ]
    action = forms.ChoiceField(choices=BACKUP_CHOICES, widget=forms.RadioSelect)
    file = forms.FileField(required=False, label='Backup File for Restore')
