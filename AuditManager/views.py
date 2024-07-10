from django.shortcuts import render
from django.http import HttpResponse
from .models import AuditLog, QueryHistory
from django.db import connection
import threading
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_informe(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="informe.pdf"'
    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, "Informe de Auditoría")
    p.showPage()
    p.save()
    return response

def listar_auditoria(request):
    logs = AuditLog.objects.all()
    return render(request, 'AuditManager/listar_auditoria.html', {'logs': logs})

def listar_consultas(request):
    consultas = QueryHistory.objects.all()
    return render(request, 'AuditManager/listar_consultas.html', {'consultas': consultas})

def ejecutar_consulta(request):
    query = "SELECT * FROM Clientes_cliente"  
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        QueryHistory.objects.create(query_sql=query, result=result)
    return HttpResponse("Consulta ejecutada y registrada")

def consulta_a():
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM Clientes_tramite")
        result = cursor.fetchone()
    return result

def consulta_b():
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM Pagos_pago")
        result = cursor.fetchone()
    return result

def comparacion_hilos(request):
    hilo_a = threading.Thread(target=consulta_a)
    hilo_b = threading.Thread(target=consulta_b)

    hilo_a.start()
    hilo_b.start()

    hilo_a.join()
    hilo_b.join()
    
    resultado_a = consulta_a()
    resultado_b = consulta_b()
    
    # Convierte los resultados a cadenas legibles
    resultado_a_str = str(resultado_a[0])
    resultado_b_str = str(resultado_b[0])
    
    # Registra los resultados en QueryHistory
    QueryHistory.objects.create(query_sql="SELECT COUNT(*) FROM Clientes_tramite", result=resultado_a_str)
    QueryHistory.objects.create(query_sql="SELECT COUNT(*) FROM Pagos_pago", result=resultado_b_str)
    
    return HttpResponse("Consultas completadas en paralelo")