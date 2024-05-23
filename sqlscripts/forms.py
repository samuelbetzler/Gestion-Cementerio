from django import forms
import os

class SQLScriptForm(forms.Form):
    scripts_dir = os.path.join(os.path.dirname(__file__), 'sql_scripts/store_procedures')
    script_files = [(f, f) for f in os.listdir(scripts_dir) if f.endswith('.sql')]
    scripts = forms.MultipleChoiceField(choices=script_files, widget=forms.CheckboxSelectMultiple)
