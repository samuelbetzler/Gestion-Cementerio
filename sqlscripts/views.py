from django.shortcuts import render, redirect
from django.db import connection
import os
from .forms import SQLScriptForm

def index(request):
    form = SQLScriptForm()
    print(form)
    return render(request, 'sqlscripts/execute_scripts.html', {'form': form})

def execute_scripts(request):
    if request.method == 'POST':
        form = SQLScriptForm(request.POST)
        if form.is_valid():
            selected_scripts = form.cleaned_data['scripts']
            scripts_dir = os.path.join(os.path.dirname(__file__), 'sql_scripts', 'store_procedures')
            errors = []
            for script_name in selected_scripts:
                script_path = os.path.join(scripts_dir, script_name)
                try:
                    with open(script_path, 'r') as file:
                        sql_script = file.read()
                        with connection.cursor() as cursor:
                            cursor.executescript(sql_script)
                except Exception as e:
                    errors.append(f"Error al ejecutar el script '{script_name}': {str(e)}")
            if errors:
                # Si se encontraron errores, puedes manejarlos de alguna manera
                # Por ejemplo, puedes mostrarlos en una página de error o redirigir a otra vista
                return render(request, 'sqlscripts/error.html', {'errors': errors})
            else:
                return redirect('sqlscripts:success')
    else:
        form = SQLScriptForm()
    return render(request, 'sqlscripts/execute_scripts.html', {'form': form})

def success(request):
    return render(request, 'sqlscripts/success.html')
