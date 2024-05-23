from django.shortcuts import render, redirect
from django.db import connection
import os
from .forms import SQLScriptForm

def index(request):
    return render(request, 'sqlscripts/index.html')

def execute_scripts(request):
    if request.method == 'POST':
        form = SQLScriptForm(request.POST)
        if form.is_valid():
            selected_scripts = form.cleaned_data['scripts']
            scripts_dir = os.path.join(os.path.dirname(__file__), 'sql_scripts/store_procedures')
            for script_name in selected_scripts:
                script_path = os.path.join(scripts_dir, script_name)
                with open(script_path, 'r') as file:
                    sql_script = file.read()
                    with connection.cursor() as cursor:
                        cursor.executescript(sql_script)
            return redirect('sqlscripts:success')
    else:
        form = SQLScriptForm()
    return render(request, 'sqlscripts/execute_scripts.html', {'form': form})

def success(request):
    return render(request, 'sqlscripts/success.html')
