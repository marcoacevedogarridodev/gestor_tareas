from django.core.management.base import BaseCommand
from tareas.models import Tarea
from django.utils import timezone

class Command(BaseCommand):
    help = 'Crea tareas de ejemplo para demostrar la aplicación'
    
    def handle(self, *args, **options):
        tareas_ejemplo = [
            {
                'titulo': 'Configurar el entorno de desarrollo Django',
                'descripcion': 'Instalar Django, crear entorno virtual y configurar el proyecto base',
                'completada': True
            },
            {
                'titulo': 'Diseñar el modelo de Tareas',
                'descripcion': 'Crear el modelo Tarea con todos los campos requeridos en español',
                'completada': True
            },
            {
                'titulo': 'Implementar vistas con HTMX',
                'descripcion': 'Crear todas las vistas necesarias para el CRUD usando HTMX para interacciones sin recarga',
                'completada': True
            },
            {
                'titulo': 'Estilizar la interfaz con Tailwind CSS',
                'descripcion': 'Aplicar estilos modernos y responsive usando Tailwind CSS',
                'completada': True
            },
            {
                'titulo': 'Crear API REST con Django REST Framework',
                'descripcion': 'Implementar endpoints API para consultar y gestionar tareas',
                'completada': True
            },
            {
                'titulo': 'Agregar funcionalidad de filtros y búsqueda',
                'descripcion': 'Implementar filtros por estado y búsqueda en tiempo real',
                'completada': True
            },
            {
                'titulo': 'Mejorar la experiencia de usuario con animaciones',
                'descripcion': 'Agregar transiciones suaves y efectos visuales',
                'completada': False
            },
            {
                'titulo': 'Escribir documentación del proyecto',
                'descripcion': 'Crear documentación completa en español para desarrolladores',
                'completada': False
            },
            {
                'titulo': 'Probar todas las funcionalidades',
                'descripcion': 'Realizar pruebas exhaustivas de todas las características implementadas',
                'completada': False
            }
        ]
        tareas_creadas = 0
        tareas_actualizadas = 0
        
        for datos_tarea in tareas_ejemplo:
            tarea, creada = Tarea.objects.get_or_create(
                titulo=datos_tarea['titulo'],
                defaults={
                    'descripcion': datos_tarea['descripcion'],
                    'completada': datos_tarea['completada'],
                    'fecha_creacion': timezone.now()
                }
            )
            if creada:
                self.stdout.write(
                    self.style.SUCCESS(f'Tarea creada: "{tarea.titulo}"')
                )
                tareas_creadas += 1
            else:
                tarea.descripcion = datos_tarea['descripcion']
                tarea.completada = datos_tarea['completada']
                tarea.save()
                self.stdout.write(
                    self.style.WARNING(f'Tarea actualizada: "{tarea.titulo}"')
                )
                tareas_actualizadas += 1
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\n¡Proceso completado! '
                f'Tareas creadas: {tareas_creadas}, '
                f'Tareas actualizadas: {tareas_actualizadas}'
            )
        )