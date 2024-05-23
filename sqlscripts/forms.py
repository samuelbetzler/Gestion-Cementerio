from django import forms
from django.conf import settings
import os

class SQLScriptForm(forms.Form):
    scripts_dir = os.path.join(settings.BASE_DIR, 'sqlscripts', 'sql_scripts', 'store_procedures')
    script_files = [(f, f) for f in os.listdir(scripts_dir) if f.endswith('.sql')]
    scripts = forms.MultipleChoiceField(choices=script_files, widget=forms.CheckboxSelectMultiple)
