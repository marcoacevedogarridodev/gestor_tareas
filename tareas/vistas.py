from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from django.utils.timezone import now
from .models import Tarea
from .forms import FormularioTarea, FormularioEditarTarea
from rest_framework import viewsets, filters
from .serializers import TareaSerializer

def lista_tareas(request):
    filtro = request.GET.get('filtro', 'todas')
    busqueda = request.GET.get('busqueda', '')
    tareas = Tarea.objects.all()
    if filtro == 'completadas':
        tareas = tareas.filter(completada=True)
    elif filtro == 'pendientes':
        tareas = tareas.filter(completada=False)
    if busqueda:
        tareas = tareas.filter(
            Q(titulo__icontains=busqueda) | 
            Q(descripcion__icontains=busqueda)
        )
    formulario_crear = FormularioTarea()
    contexto = {
        'tareas': tareas,
        'filtro_actual': filtro,
        'busqueda_actual': busqueda,
        'total_tareas': tareas.count(),
        'tareas_completadas': tareas.filter(completada=True).count(),
        'tareas_pendientes': tareas.filter(completada=False).count(),
        'formulario': formulario_crear,
    }
    return render(request, 'tareas/lista_tareas.html', contexto)

@require_http_methods(["POST"])
def crear_tarea(request):
    formulario = FormularioTarea(request.POST)
    if formulario.is_valid():
        tarea = formulario.save()
        return render(request, 'tareas/tarea_parcial.html', {'tarea': tarea})
    return render(request, 'tareas/formulario_tarea.html', {
        'formulario': formulario,
        'accion': 'crear'
    }, status=400)

@require_http_methods(["GET"])
def formulario_editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    formulario = FormularioEditarTarea(instance=tarea)
    return render(request, 'tareas/formulario_tarea.html', {
        'formulario': formulario,
        'tarea': tarea,
        'accion': 'editar'
    })

@require_http_methods(["POST"])
def actualizar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    formulario = FormularioEditarTarea(request.POST, instance=tarea)
    
    if formulario.is_valid():
        tarea = formulario.save()
        return render(request, 'tareas/tarea_parcial.html', {'tarea': tarea})
    
    return render(request, 'tareas/formulario_tarea.html', {
        'formulario': formulario,
        'tarea': tarea,
        'accion': 'editar'
    }, status=400)

@require_http_methods(["POST"])
def alternar_estado_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.completada = not tarea.completada
    tarea.save()
    return render(request, 'tareas/tarea_parcial.html', {'tarea': tarea})

@require_http_methods(["DELETE"])
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.delete()
    return JsonResponse({
        'success': True, 
        'message': 'Tarea eliminada correctamente'
    })

def obtener_estadisticas(request):
    total = Tarea.objects.count()
    completadas = Tarea.objects.filter(completada=True).count()
    pendientes = Tarea.objects.filter(completada=False).count()
    
    return JsonResponse({
        'total': total,
        'completadas': completadas,
        'pendientes': pendientes,
        'porcentaje_completadas': round((completadas / total * 100), 2) if total > 0 else 0
    })

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo', 'descripcion']
    ordering_fields = ['fecha_creacion', 'fecha_actualizacion', 'completada']
    ordering = ['-fecha_creacion']