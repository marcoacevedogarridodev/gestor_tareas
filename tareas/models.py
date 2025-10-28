from django.db import models
from django.utils import timezone

class Tarea(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
    ]
    titulo = models.CharField(max_length=200, verbose_name="Título", help_text="Ingresa un título descriptivo para la tarea")
    descripcion = models.TextField(blank=True, verbose_name="Descripción", help_text="Describe los detalles de la tarea (opcional)")
    completada = models.BooleanField(default=False, verbose_name="Completada")
    fecha_creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    
    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ['-fecha_creacion']
    
    def estado_display(self):
        return "Completada" if self.completada else "Pendiente"