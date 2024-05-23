from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .utils import render_to_pdf  
from Clientes.models import Cliente
from Difuntos.models import Difunto, CausaMuerte
from Personal.models import Personal, TipoPersonal
from Estructuras.models import Estructura
from Ubicaciones.models import Ubicacion, Provincia, Canton
from Certificados.models import Certificado
from Pagos.models import Pago
from Incidentes.models import TipoIncidente, ReporteIncidente

def index(request):
    entidades = [
        'clientes',
        'difuntos',
        'personal',
        'estructuras',
        'ubicaciones',
        'certificados',
        'pagos',
        'incidentes',
    ]
    return render(request, 'Generator/selector_sections.html', {'entidades': entidades})

def generar_reporte(request):
    selected_sections = request.POST.getlist('sections')
    context = {'sections': selected_sections}
    
    if 'clientes' in selected_sections:
        context['clientes'] = Cliente.objects.all()
    if 'difuntos' in selected_sections:
        difuntos = Difunto.objects.select_related('id_cau_mue').all()
        context['difuntos'] = difuntos
    if 'personal' in selected_sections:
        personal = Personal.objects.select_related('id_tipo_per').all()
        context['personal'] = personal
    if 'estructuras' in selected_sections:
        estructuras = Estructura.objects.select_related('id_lugar_estruc', 'id_tipo_estruc', 'id_est_estruc').all()
        context['estructuras'] = estructuras
    if 'ubicaciones' in selected_sections:
        ubicaciones = Ubicacion.objects.select_related('id_pro', 'id_can').all()
        context['ubicaciones'] = ubicaciones
    if 'certificados' in selected_sections:
        certificados = Certificado.objects.select_related('id_tram').all()
        context['certificados'] = certificados
    if 'pagos' in selected_sections:
            pagos = Pago.objects.select_related('id_tipo_pago', 'id_tram').all()
            context['pagos'] = pagos
    if 'incidentes' in selected_sections:
        incidentes = ReporteIncidente.objects.select_related('id_tipo_inci', 'id_per').all()
        context['incidentes'] = incidentes
    pdf = render_to_pdf('Generator/pdf_template.html', context)
    return HttpResponse(pdf, content_type='application/pdf')
