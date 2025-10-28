from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    estado_display = serializers.ReadOnlyField()
    fecha_creacion_formateada = serializers.SerializerMethodField()
    
    class Meta:
        model = Tarea
        fields = [
            'id', 
            'titulo', 
            'descripcion', 
            'completada', 
            'estado_display',
            'fecha_creacion', 
            'fecha_creacion_formateada',
            'fecha_actualizacion'
        ]
        read_only_fields = ['id', 'fecha_creacion', 'fecha_actualizacion']
    
    def get_fecha_creacion_formateada(self, obj):
        return obj.fecha_creacion.strftime("%d/%m/%Y %H:%M")