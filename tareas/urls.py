from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import vistas

router = DefaultRouter()
router.register(r'api/tareas', vistas.TareaViewSet)

urlpatterns = [
    path('', vistas.lista_tareas, name='lista_tareas'),
    path('crear/', vistas.crear_tarea, name='crear_tarea'),
    path('<int:id>/editar-formulario/', vistas.formulario_editar_tarea, name='formulario_editar_tarea'),
    path('<int:id>/actualizar/', vistas.actualizar_tarea, name='actualizar_tarea'),
    path('<int:id>/alternar-estado/', vistas.alternar_estado_tarea, name='alternar_estado_tarea'),
    path('<int:id>/eliminar/', vistas.eliminar_tarea, name='eliminar_tarea'),
    path('estadisticas/', vistas.obtener_estadisticas, name='obtener_estadisticas'),
    path('', include(router.urls)),
]